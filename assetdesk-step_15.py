# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: AssetDesk
class CommandDispatcher:
    def __init__(self, handlers):
        self._handlers = {cmd.lower(): handler for cmd, handler in handlers.items()}

    def dispatch(self, text):
        clean_text = text.strip().lower()
        if clean_text.startswith("help"):
            print("\nAvailable commands:")
            for cmd in sorted(self._handlers.keys()):
                print(f"  {cmd}")
            return True
        handler = self._handlers.get(clean_text)
        if handler:
            try:
                result = handler()
                if isinstance(result, str):
                    print(result)
                elif result is not None:
                    print("Command executed successfully.")
                else:
                    print("No output from command.")
                return True
            except Exception as e:
                print(f"Error executing '{clean_text}': {e}")
                return False
        if clean_text.startswith("-"):
            print(f"Unknown option or flag: {text}")
            return False
        print(f"Unknown command: {text}. Type 'help' for a list.")
        return False
