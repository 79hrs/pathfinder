#!/usr/bin/env python3

import os
import sys
import subprocess

def find_project_root(start_path, root_marker):
	"""Finds the root dirctory using the .root file as a marker."""
	if start_path is None:
		start_path = os.getcwd()

	current_directory = start_path

	while True:
		if os.path.isfile(os.path.join(current_directory, root_marker)):
			return current_directory
		parent_directory = os.path.dirname(current_directory)
		if parent_directory == current_directory:
			return None		# if this is true, we have reached the root of the filesystem.

		current_directory = parent_directory

def find_script_name_in_project(script_name, project_root):
	for root, _, files in os.walk(project_root):
		if script_name in files:
			return os.path.join(root, script_name)
	return None

def add_all_subdirectories_to_path(project_root):
	subdirs = [project_root]
	for root, dirs, _ in os.walk(project_root):
		for directory in dirs:
			subdirs.append(os.path.join(root, directory))
	return subdirs

def main():
	project_root = find_project_root(start_path=None, root_marker='.root')
	if not project_root:
		print("Error: Could not find the project root(no .root file)", file = sys.stderr)
		sys.exit(1)

	all_paths = add_all_subdirectories_to_path(project_root)
	env = os.environ.copy()
	env["PYTHONPATH"] = os.pathsep.join(all_paths) + os.pathsep + env.get("PYTHONPATH", "")

	sys.path[:0] = all_paths

	if len(sys.argv) < 2:
		print("Usage: pathfinder <script.py> [args...]")
		sys.exit(1)

	script = sys.argv[1]

	if os.path.isfile(os.path.join(project_root, script)):
		script_path = os.path.join(project_root, script)
	else:
		print("Script does not exist in the root directory. Searching in the subdirectories...")
		script_path = find_script_name_in_project(script, project_root)
		if script_path is None:
			print(f"Could not find {script} in the project.")
			sys.exit(1)

	subprocess.run([sys.executable, script_path, *sys.argv[2:]], env=env)

if __name__ == "__main__":
	main()
