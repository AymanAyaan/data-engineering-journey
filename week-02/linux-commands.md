
1. Inspecting Files

• ls -lh <file>: Checks the file size in a human-readable format (e.g., KB, MB).
• wc -l <file>: Counts the total number of lines in a file.
• head -n <file>: Displays the first n lines of a file (e.g., head -3 shows the top 3 lines) to inspect its structure.
• tail -n <file>: Displays the last n lines of a file.
• cat <file>: Prints the entire content of a file to the terminal.

2. Searching & Filtering (grep)

• grep "pattern" <file>: Searches for and prints lines matching a specific text pattern.
• grep -c "pattern" <file>: Counts how many lines match the given pattern (e.g., grep -c "| ERROR |" app.log).
• grep -v "pattern": Inverts the match to exclude lines containing the pattern.
• grep "^2026-10-17": Uses ^ to match lines that start with a specific date.

3. Extracting & Cleaning Text (cut & tr)

• cut -c1-10: Extracts characters from position 1 to 10 on each line (used to grab the date YYYY-MM-DD, or cut -c12-13 for the hour).
• cut -d'|' -f3: Splits each line using the pipe (|) delimiter and extracts the 3rd field (such as the log level or component).
• tr -d ' ': Deletes extra whitespace characters from the output.

4. Sorting & Counting (sort & uniq)

• sort: Sorts lines alphabetically or numerically. This is required before running uniq.
• uniq -c: Counts consecutive duplicate lines and prefixes each line with its occurrence count.
• sort -rn: Sorts lines in reverse (-r) numerical (-n) order so the highest counts appear at the top.

5. Pipes & Redirection

• | (Pipe): Sends the output of one command directly as the input into the next command.
• > (Overwrite): Writes command output into a new file, overwriting any existing content.
• >> (Append): Adds command output to the end of an existing file without deleting old content.

These are all commands we acquired in class 2
