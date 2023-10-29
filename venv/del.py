import os
def dele():
        for i in range(13):
            try:
                os.remove('output' + str(i) + '.pdf')
                print("deleted!")
            except:
                break

if __name__ == "__main__":
    dele()