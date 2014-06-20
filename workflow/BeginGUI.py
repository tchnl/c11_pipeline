import Tkinter as tkinter


class MyGUI:

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Motif finder v1.0")
        
        self.top_frame = tkinter.Frame(self.main_window)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)
        self.__value = 1
        
        self.label1 = tkinter.Label(self.top_frame, text = "Choose one of the following options")
        self.label2 = tkinter.Label(self.top_frame, text = "\n")

        self.rb1 = tkinter.Radiobutton(self.top_frame, text = "All modules without Sort", variable=self.radio_var, value=1)
        self.rb2 = tkinter.Radiobutton(self.top_frame, text = "All modules include Sort", variable=self.radio_var, value=2)
        self.rb3 = tkinter.Radiobutton(self.top_frame, text = "Select individual modules", variable=self.radio_var, value=3)
        
        self.my_button = tkinter.Button(self.main_window, text = "Ok", command=self.show_choice)
                
        self.label1.pack()
        self.label2.pack()
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        self.my_button.pack(side='bottom')

        self.top_frame.pack()
        
        
        tkinter.mainloop()
        

    def show_choice(self):
        if self.radio_var.get() == 1:
            self.__value = 1
        if self.radio_var.get() == 2:
            self.__value = 2
        if self.radio_var.get() == 3:
            self.__value = 3
        self.main_window.destroy()
        
        

    def get_value(self):
        return self.__value




class MyGUI2:

    def __init__(self):
        self.main_window = tkinter.Tk()
        
        self.label = tkinter.Label(self.main_window, text = "Insert the filenames for the required files below:")
        self.label2 = tkinter.Label(self.main_window, text = "File with ratios:")
        self.label3 = tkinter.Label(self.main_window, text = "File with orthologues:")
        self.label4 = tkinter.Label(self.main_window, text = "File with sequences from strain WCFS1 replicate 1:")
        self.label5 = tkinter.Label(self.main_window, text = "File with sequences from strain WCFS1 replicate 2:")
        self.label6 = tkinter.Label(self.main_window, text = "File with sequences from strain NC8 replicate 1:")
        self.label7 = tkinter.Label(self.main_window, text = "File with sequences from strain NC8 replicate 2:")
        self.entry = tkinter.Entry(self.main_window, width = 40)
        self.entry2 = tkinter.Entry(self.main_window, width = 40)
        self.entry3 = tkinter.Entry(self.main_window, width = 40)
        self.entry4 = tkinter.Entry(self.main_window, width = 40)
        self.entry5 = tkinter.Entry(self.main_window, width = 40)
        self.entry6 = tkinter.Entry(self.main_window, width = 40)
        self.my_button2 = tkinter.Button(self.main_window, text = "Ok", command= self.invoer)                 
        
        self.label.pack()
        self.label2.pack()
        self.entry.pack()
        self.label3.pack()
        self.entry2.pack()
        self.label4.pack()
        self.entry3.pack()
        self.label5.pack()
        self.entry4.pack()
        self.label6.pack()
        self.entry5.pack()
        self.label7.pack()
        self.entry6.pack()
        self.my_button2.pack()


        tkinter.mainloop()

    def invoer(self):
        self.lijst = []
        bestRatio = str(self.entry.get())
        bestGenen = str(self.entry2.get())
        bestSeq1 = str(self.entry3.get())
        bestSeq2 = str(self.entry4.get())
        bestSeq3 = str(self.entry5.get())
        bestSeq4 = str(self.entry6.get())

        self.lijst.append(bestRatio)
        self.lijst.append(bestGenen)
        self.lijst.append(bestSeq1)
        self.lijst.append(bestSeq2)
        self.lijst.append(bestSeq3)
        self.lijst.append(bestSeq4)
        self.main_window.destroy()
        

    def get_file(self):
        return self.lijst

    

class MyGUI3:

    def __init__(self):
        self.main_window = tkinter.Tk()
        
        self.radio_var = tkinter.IntVar()
        self.radio_var.set(4)
        self.__module = 4

        self.label = tkinter.Label(self.main_window, text = "Select one of the modules below:")
        self.rb1 = tkinter.Radiobutton(self.main_window, text = "Filter ratios", variable=self.radio_var, value=4)
        self.rb2 = tkinter.Radiobutton(self.main_window, text = "Sort ratios", variable=self.radio_var, value=5)
        self.rb3 = tkinter.Radiobutton(self.main_window, text = "NZ/NC convert", variable=self.radio_var, value=6)
        self.rb4 = tkinter.Radiobutton(self.main_window, text = "FASTA files maker", variable=self.radio_var, value=7)
        self.rb5 = tkinter.Radiobutton(self.main_window, text = "MEME", variable=self.radio_var, value=8)

        self.my_button3 = tkinter.Button(self.main_window, text = "Ok", command= self.module)                 

        self.label.pack()
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        self.rb4.pack()
        self.rb5.pack()
        self.my_button3.pack()

        tkinter.mainloop()

    def module(self):
        if self.radio_var.get() == 4:
            self.__module = 4
        if self.radio_var.get() == 5:
            self.__module = 5
        if self.radio_var.get() == 6:
            self.__module = 6
        if self.radio_var.get() == 7:
            self.__module = 7
        if self.radio_var.get() == 8:
            self.__module = 8

        self.main_window.destroy()

    def get_module(self):
        return self.__module


class MyGUI4:

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.label = tkinter.Label(self.main_window, text = "Insert the filename for the required file below:")
        self.label2 = tkinter.Label(self.main_window, text = "File with ratios:")
        self.entry = tkinter.Entry(self.main_window, width = 40)
        self.my_button3 = tkinter.Button(self.main_window, text = "Ok", command= self.invoer)                 


        self.label.pack()
        self.label2.pack()
        self.entry.pack()
        self.my_button3.pack()
        tkinter.mainloop()

    def invoer(self):
        self.lijst = []
        bestRatio = str(self.entry.get())
        self.lijst.append(bestRatio)
        self.main_window.destroy()

    def get_file(self):
        return self.lijst

class MyGUI5:

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.label = tkinter.Label(self.main_window, text = "Insert the filename for the required file below:")
        self.label2 = tkinter.Label(self.main_window, text = "File with (Filtered) ratios:")
        self.entry = tkinter.Entry(self.main_window, width = 40)
        self.my_button3 = tkinter.Button(self.main_window, text = "Ok", command= self.invoer)                 


        self.label.pack()
        self.label2.pack()
        self.entry.pack()
        self.my_button3.pack()
        tkinter.mainloop()

    def invoer(self):
        self.lijst = []
        bestRatio = str(self.entry.get())
        self.lijst.append(bestRatio)
        self.main_window.destroy()

    def get_file(self):
        return self.lijst

class MyGUI6:

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.label = tkinter.Label(self.main_window, text = "Insert the filename for the required file below:")
        self.label2 = tkinter.Label(self.main_window, text = "File with orthologues:")
        self.entry = tkinter.Entry(self.main_window, width = 40)
        self.my_button3 = tkinter.Button(self.main_window, text = "Ok", command= self.invoer)                 


        self.label.pack()
        self.label2.pack()
        self.entry.pack()
        self.my_button3.pack()
        tkinter.mainloop()

    def invoer(self):
        self.lijst = []
        bestRatio = str(self.entry.get())
        self.lijst.append(bestRatio)
        self.main_window.destroy()

    def get_file(self):
        return self.lijst

class MyGUI7:

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.label = tkinter.Label(self.main_window, text = "Insert the filenames for the required files below:")
        self.label2 = tkinter.Label(self.main_window, text = "File with (Filtered/sorted) ratios:")
        self.label3 = tkinter.Label(self.main_window, text = "File with orthologues:")
        self.label4 = tkinter.Label(self.main_window, text = "File with sequences from strain WCFS1 replicate 1:")
        self.label5 = tkinter.Label(self.main_window, text = "File with sequences from strain WCFS1 replicate 2:")
        self.label6 = tkinter.Label(self.main_window, text = "File with sequences from strain NC8 replicate 1:")
        self.label7 = tkinter.Label(self.main_window, text = "File with sequences from strain NC8 replicate 2:")
        self.entry = tkinter.Entry(self.main_window, width = 40)
        self.entry2 = tkinter.Entry(self.main_window, width = 40)
        self.entry3 = tkinter.Entry(self.main_window, width = 40)
        self.entry4 = tkinter.Entry(self.main_window, width = 40)
        self.entry5 = tkinter.Entry(self.main_window, width = 40)
        self.entry6 = tkinter.Entry(self.main_window, width = 40)
        self.my_button2 = tkinter.Button(self.main_window, text = "Ok", command= self.invoer)                 
        
        self.label.pack()
        self.label2.pack()
        self.entry.pack()
        self.label3.pack()
        self.entry2.pack()
        self.label4.pack()
        self.entry3.pack()
        self.label5.pack()
        self.entry4.pack()
        self.label6.pack()
        self.entry5.pack()
        self.label7.pack()
        self.entry6.pack()
        self.my_button2.pack()
        
        tkinter.mainloop()

    def invoer(self):
        self.lijst = []
        bestRatio = str(self.entry.get())
        bestGenen = str(self.entry2.get())
        bestSeq1 = str(self.entry3.get())
        bestSeq2 = str(self.entry4.get())
        bestSeq3 = str(self.entry5.get())
        bestSeq4 = str(self.entry6.get())

        self.lijst.append(bestRatio)
        self.lijst.append(bestGenen)
        self.lijst.append(bestSeq1)
        self.lijst.append(bestSeq2)
        self.lijst.append(bestSeq3)
        self.lijst.append(bestSeq4)
        self.main_window.destroy()

    def get_file(self):
        return self.lijst

class MyGUI8:

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.label = tkinter.Label(self.main_window, text = "Insert the filename for the required file below:")
        self.label2 = tkinter.Label(self.main_window, text = "Outputfile from FASTA files maker:")
        self.entry = tkinter.Entry(self.main_window, width = 40)
        self.my_button3 = tkinter.Button(self.main_window, text = "Ok", command= self.invoer)                 


        self.label.pack()
        self.label2.pack()
        self.entry.pack()
        self.my_button3.pack()
        tkinter.mainloop()

    def invoer(self):
        self.lijst = []
        bestRatio = str(self.entry.get())
        self.lijst.append(bestRatio)
        self.main_window.destroy()

    def get_file(self):
        return self.lijst
        

def main():
    my_gui = MyGUI()
        
    if my_gui.get_value() == 1:
        my_gui2 = MyGUI2()
        lijst2 = my_gui2.get_file()
        lijst2.append(1)
        return lijst2
    elif my_gui.get_value() == 2:
        my_gui2 = MyGUI2()
        lijst2 = my_gui2.get_file()
        lijst2.append(2)
        return lijst2
    elif my_gui.get_value() == 3:
        my_gui3 = MyGUI3()
        if my_gui3.get_module() == 4:
            my_gui4 = MyGUI4()
            lijst2 = my_gui4.get_file()
            lijst2.append(4)
            return lijst2
        elif my_gui3.get_module() == 5:
            my_gui5 = MyGUI5()
            lijst2 = my_gui5.get_file()
            lijst2.append(5)
            return lijst2
        elif my_gui3.get_module() == 6:
            my_gui6 = MyGUI6()
            lijst2 = my_gui6.get_file()
            lijst2.append(6)
            return lijst2
        elif my_gui3.get_module() == 7:
            my_gui7 = MyGUI7()
            lijst2 = my_gui7.get_file()
            lijst2.append(7)
            return lijst2
        elif my_gui3.get_module() == 8:
            my_gui8 = MyGUI8()
            lijst2 = my_gui8.get_file()
            lijst2.append(8)
            return lijst2

main()

