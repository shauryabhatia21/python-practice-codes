"""
Launcher for Cyber Nova: Galaxy Striker.
Allows launching directly from workspace root.
"""
import os
import sys
import importlib.util

game_dir = os.path.join(os.path.dirname(__file__), "GAME")
if not os.path.isdir(game_dir):
    game_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "GAME"))

if game_dir not in sys.path:
    sys.path.insert(0, game_dir)

target_file = os.path.join(game_dir, "shooting_game.py")
spec = importlib.util.spec_from_file_location("shooting_game_mod", target_file)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
CyberNovaGame = mod.CyberNovaGame

if __name__ == "__main__":
    game = CyberNovaGame()
    game.run()
