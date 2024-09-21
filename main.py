from GUI import GUI_mainloop

if __name__ == "__main__":
    try:
        GUI_mainloop()
    except Exception as e:
        print("Error:", str(e))
