import os
import platform
system = platform.system
system = platform.system()
def shutdown() -> str:
    response = input("Do you want to shut down? (yes/no): ")
    match response:
        case "yes":
            return "shutting down"
        case "no":
            return "not shutting down"
        case _:
            return "invalid input"
def main():       
        result = shutdown() 
        if result == "shutting down":
          print("System is shutting down...")
          os.system("shutdown /s /t 10")   
        elif result == "not shutting down":
            print("Shutdown aborted.")
        else:
            print("Sorry, unrecognized input.")

if __name__ == "__main__":
    main()