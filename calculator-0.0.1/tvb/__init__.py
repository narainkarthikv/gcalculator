from __future__ import print_function
import argparse
print("The Virtual Brain imported!")
def parse_args():
 parser = argparse.ArgumentParser()
 parser.add_argument("text", help="Text to TVB-Neuropackage")
 return parser.parse_args()
def main():
 print("This is the main function :)")
 args = parse_args()
 print(args.text)
