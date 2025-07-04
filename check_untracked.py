import subprocess #library to allow you to write command on terminal 
import os #to open files 
import fnmatch # library that lets you test filenames against shell-style glob patterns (*.db, images/*.png, etc.).





# creating a function for extracting all the filters and puting them in a list 
def get_lfs_patterns():
    patterns = []
    if os.path.exists(".gitattributes"): # checks if there is a lsf atribute file in the repo  
        with open(".gitattributes", "r") as f: # opens it if that the case 
            for line in f: 
                if "filter=lfs" in line:
                    pattern = line.split()[0] #splits the row by spaces and give the fist string because line is 1 whole string 
                    patterns.append(pattern)
    return patterns



# creating a function for getting all untracted files and returning them into a list 
def get_untracked_files():
    """
    Runs 'git ls-files --others --exclude-standard' to list files
    not tracked by Git (and not ignored). Returns a list of file paths.
    """
    ans  = "git ls-files --others --exclude-standard" #this the command to give all the untracked file in dir 
    
    # subprocess.run returns a CompletedProcess object with:
    # - args: the command run
    # - returncode: exit code of the command
    # - stdout: standard output (here, our file list as a multiline string)
    # - stderr: standard error output

    result = subprocess.run(
        ans.split(), # doing this because subprossess takes a list for out puting 
        capture_output=True,   # capture the command's text output
        text=True              # interpret the output as text (not bytes)
    )
    # Convert to a list of filenames using split lines because it split on the "/n"  not " " so that files with spaces dont get seperated
    return result.stdout.strip().splitlines()


# this function checks if the file name is one of the files thats already tracked 
def is_tracked_by_lfs(filename, patterns):
    """
    Returns True if filename matches any glob in patterns.
    fnmatch.fnmatch('movies.db', '*.db') -> True
    """
    for pat in patterns:
        if fnmatch.fnmatch(filename, pat):
            return True
    return False


if __name__ == "__main__":
    # 1) List all untracked files
    untracked = get_untracked_files()

    # 2) Get patterns already tracked by Git LFS
    lfs_patterns = get_lfs_patterns()

    # 3) Filter: keep only files that are
    #     a) not covered by LFS
    #     b) larger than 100 MB
    to_report = []

    for f in untracked:
        # Check if file matches an LFS pattern
        if is_tracked_by_lfs(f, lfs_patterns):
            continue
        # Check file size
        try:
            size = os.path.getsize(f)
        except OSError:
            # Skip if file not accessible
            continue
        if size > 100 * 1024 * 1024:
            to_report.append(f)

    # 4) Report
    if to_report:
        print('do " git lfs track "*.mp3" " to track the big files ')
        print("Untracked large files (>100MB) not covered by LFS:")
        for f in to_report:
            print("  -", f)
    else:
        print("No untracked files over 100MB outside of LFS found.")




