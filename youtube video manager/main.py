import json

def show_menu():
    print("Choose an option below. ")
    print("1. list all videos")
    print("2. add a video")
    print("3. update a yt video details")
    print("4. delete a video")
    print("5. exit the app")


def load_data():
        try:
            with open('youtube.txt','r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

# thi is a helper function for saving the videos to file
def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_of_all_videos(videos):
    print("\n")
    print("*"*70)
    for index,video_desc in enumerate(videos,start=1):
        print(f"{index}: {video_desc['name']}, Duration: {video_desc['time']}")
    print("*" * 70)

def add_video(videos):
    name = input("Enter the video name: ")
    time = input("Enter the video time: ")
    videos.append({'name':name, 'time':time})
    save_data_helper(videos)

# we are storing the data into this format
# [{ name:'yt name', time:"12 mins"},{}]


def update_video_details(videos):
    list_of_all_videos(videos)
    index = int(input("Enter the video number to be Update: "))

    if 1 <= index <= len(videos):
        name = input("Enter the name ")
        time = input("Enter the time ")
        videos[index-1] = {"name":name, "time":time}

        save_data_helper(videos)
    else:
        print("Invalid video number, Please try again!.")

def delete_video(videos):
    list_of_all_videos(videos)
    index = int(input("Enter the video number to be Deleted: "))

    if 1 <= index <= len(videos):
        del videos[index - 1 ]
        print(f'{index}th video deleted successfully')
        save_data_helper(videos)
    else:
        print("Invalid video number, Please try again!.")

def exit_app():
    exit()
    
def main():
    videos = load_data()
    
    print(" "*20,"YOUTUBE MANAGER")
    while True:
        print("*"* 75)
        show_menu()
        choice = input("Enter your choice: ")
        
        match choice:
            case "1":
                print("list of all videos")
                list_of_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                print("update a yt video details")
                update_video_details(videos)
            case "4":
                print("delete a video")
                delete_video(videos)
            case "5":
                print("exit the app")
                exit_app()
            case _:
                print("invalid choice")
        
if __name__ == "__main__":
    main()