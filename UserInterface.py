from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
import tkintermapview
from AStar import AStar
from GreedySearch import GreedySearch
from DepthFirst import DepthFirst
from UCS import UCS

class UserInterface:
    def __init__(self, map) -> None:
        self.map = map

        root = Tk()
        root.title("Mapa de " + map.name)
        root.geometry("1280x720")
        self.root = root

        left_frame = Frame(root, width=200)
        left_frame.pack(side=LEFT, fill=Y, padx=10, pady=10)
        self.left_frame = left_frame

        start_label = Label(left_frame, text="Cidade de partida")
        start_label.pack(pady=5)
        self.start_label = start_label
        start_combo_box = ttk.Combobox(left_frame, width=20)
        start_combo_box.pack(pady=10)
        start_combo_box["values"] = tuple(map.getCities())
        start_combo_box.set("Viseu")
        self.start_combo_box = start_combo_box

        end_label = Label(left_frame, text="Cidade de chegada")
        end_label.pack(pady=5)
        self.end_label = end_label
        end_combo_box = ttk.Combobox(left_frame, width=20)
        end_combo_box.pack(pady=10)
        end_combo_box["values"] = tuple(map.getCities())
        end_combo_box.set("Lisboa")
        self.end_combo_box = end_combo_box

        algorithm_label = Label(left_frame, text="Algoritmo")
        algorithm_label.pack(pady=5)
        self.algorithm_label = algorithm_label
        algorithm_combo_box = ttk.Combobox(left_frame, width=20)
        algorithm_combo_box.pack(pady=10)
        algorithm_combo_box["values"] = ("Depth First", "UCS", "A*","Greedy Search")
        algorithm_combo_box.set("A*")
        self.algorithm_combo_box = algorithm_combo_box

        map_widget = tkintermapview.TkinterMapView(root)
        map_widget.pack(expand=True, fill="both", side=RIGHT)
        self.map_widget = map_widget

        calculate_button = Button(left_frame, text="Calcular Caminho", command=self.calculate_path)
        calculate_button.pack(pady=10)
        self.calculate_button = calculate_button

        spacing_label = Label(left_frame, text="")
        spacing_label.pack(pady=10)

        path_tree = ttk.Treeview(left_frame, columns=("", "Cidade", "Distância"), show="headings")
        path_tree.column("", width=60)
        path_tree.column("Cidade", width=100)
        path_tree.heading("Cidade", text="Cidade", anchor=W)
        path_tree.column("Distância", width=100)
        path_tree.heading("Distância", text="Distância", anchor=W)
        path_tree.pack(pady=10)
        self.path_tree = path_tree

        map_widget.set_position(39.3999, -8.2245)
        map_widget.set_zoom(6)

        distance_label = Label(left_frame, text="Distância: ")
        distance_label.pack(pady=5)
        self.distance_label = distance_label

    def get_start_city_name(self):
        return self.start_combo_box.get()

    def get_end_city_name(self):
        return self.end_combo_box.get()
    
    def get_algorithm_name(self):
        return self.algorithm_combo_box.get()
    
    def mainloop(self):
        self.root.mainloop()

    def calculate_path(self):
        print(self.get_start_city_name(), self.get_end_city_name(), self.get_algorithm_name())

        start = self.map.getCity(self.get_start_city_name())
        end = self.map.getCity(self.get_end_city_name())

        if start is None or end is None:
            messagebox.showerror("Erro", "Cidade não encontrada.")
            return
        if start == end:
            messagebox.showerror("Erro", "A cidade de partida e de chegada não podem ser iguais.")
            return

        algorithm_class = None
        algorithm_name = self.get_algorithm_name()

        if algorithm_name == "Depth First":
            algorithm_class = DepthFirst()
        elif algorithm_name == "UCS":
            algorithm_class = UCS()
        elif algorithm_name == "A*":
            algorithm_class = AStar()
        elif algorithm_name == "Greedy Search":
            algorithm_class = GreedySearch()

        if algorithm_class is None:
            messagebox.showerror("Erro", "Algoritmo não encontrado.")
            return

        path, distance = algorithm_class.getPath(start, end)

        self.distance_label.config(text="Distância: " + str(distance) + " km")

        path_position_list = []

        self.map_widget.delete_all_marker()
        self.path_tree.delete(*self.path_tree.get_children())

        for i in range(len(path)):
            city = path[i]
            distance_to_previous = 0

            if i > 0:
                distance_to_previous = city.getDistance(path[i - 1])
            self.map_widget.set_marker(city.location[0], city.location[1], city.name)
            path_position_list.append(city.location)
            self.path_tree.insert("", "end", values=("Origem" if i == 0 else ("Destino" if i == len(path)-1 else ""), city.name, str(distance_to_previous) + " km"))

        self.map_widget.delete_all_path()
        path_1 = self.map_widget.set_path(path_position_list)

        for item in path:
            print (item.name)
        print(distance)
