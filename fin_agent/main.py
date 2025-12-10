import sys
import argparse
import colorama
from colorama import Fore, Style
from fin_agent.agent.core import FinAgent
from fin_agent.config import Config
from importlib.metadata import version, PackageNotFoundError

# Initialize colorama
colorama.init()

def get_version():
    try:
        return version("fin-agent")
    except PackageNotFoundError:
        return "unknown (dev)"

def main():
    parser = argparse.ArgumentParser(description="Fin-Agent: Financial Analysis AI Agent")
    parser.add_argument("-v", "--version", action="store_true", help="Show version number and exit")
    
    # Use parse_known_args so that if we want to add other args later or if existing logic uses sys.argv it doesn't break
    # But for now, we only have -v. 
    # If we use parse_args(), it will process flags. If no flags, we continue to interactive mode.
    args, unknown = parser.parse_known_args()

    if args.version:
        print(f"fin-agent version {get_version()}")
        sys.exit(0)

    print(f"{Fore.CYAN}Welcome to Fin-Agent (v{get_version()})!{Style.RESET_ALL}")
    
    # Check configuration and setup if needed
    try:
        Config.validate()
    except ValueError:
        print(f"{Fore.YELLOW}Environment variables missing. Initiating setup...{Style.RESET_ALL}")
        Config.setup()

    print("I can help you analyze stocks and provide recommendations using Tushare data and DeepSeek LLM.")
    print("Type 'exit' or 'quit' to end the session.")

    try:
        agent = FinAgent()
    except Exception as e:
         print(f"{Fore.RED}Failed to initialize Agent: {e}{Style.RESET_ALL}")
         sys.exit(1)

    while True:
        try:
            user_input = input(f"\n{Fore.GREEN}You: {Style.RESET_ALL}")
            if user_input.lower() in ['exit', 'quit']:
                print("Goodbye!")
                break
            
            if not user_input.strip():
                continue

            response = agent.run(user_input)
            print(f"\n{Fore.MAGENTA}Agent:{Style.RESET_ALL}\n{response}")

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
