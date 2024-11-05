import json;


def load_data():
        try:
            with open('youtube.txt','r') as file;
                return json.load(file)
        except FileNotFoundError:
            pass


def show_menu():
    print("Choose an option below:")
    print("1. list all videos")
    print("2. add a video")
    print("3. update a yt video details")
    print("4. delete a video")
    print("5. exit the app")

def list_of_all_videos(videos):
    pass;

def add_video(videos):
    pass;

def update_video_details(videos):
    pass;

def delete_video(videoss):
    pass;

def exit_app():
    exit();
    
def main():
    videos = load_data();
    
    print(" "*20,"YOUTUBE MANAGER")
    while True:
        print("*"* 75)
        show_menu();
        choice = input("Enter your choice")
        
        match choice:
            case "1":
                print("list of all videos")
                list_of_all_videos(videos);
            case "2":
                add_video(videos);
            case "3":
                print("update a yt video details")
                update_video_details(index);
            case "4":
                print("delete a vidoe")
                delete_video(index);
            case "5":
                print("exit the app")
                exit_app();
            case _:
                print("invalid choice")
        
if __name__ == "__main__":
    main();