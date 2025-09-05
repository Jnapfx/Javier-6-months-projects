# 🖥️ Unix_2 – Intermediate Unix Command Line Guide

This guide builds on the basics and introduces more advanced Unix commands and concepts. Learn how to manage files and directories more efficiently, customize your shell environment, and better understand how Unix operates under the hood.

---

## 📁 Commands

Master the use of these powerful commands:

- `cp` – Copy files or directories  
  Example:  
  ```bash
  cp file.txt backup/
  ```

- `mkdir` – Create new directories  
  Example:  
  ```bash
  mkdir new_folder
  ```

- `less` – View the contents of a file one page at a time  
  Example:  
  ```bash
  less long_text.txt
  ```

- `mv` – Move or rename files and directories  
  Example:  
  ```bash
  mv oldname.txt newname.txt
  ```

- `rm` – Remove files or directories  
  Example:  
  ```bash
  rm unwanted_file.txt
  ```

---

## 🧾 Arguments

Use multiple arguments and combine arguments with options:

- Multiple arguments:  
  ```bash
  cp file1.txt file2.txt /destination/
  ```

- Argument to an option:  
  ```bash
  ls -d foldername/
  ```

---

## 🐚 Kernels and Shells

Understand and work with Unix shells:

- Access the default shell:  
  ```bash
  echo $SHELL
  ```

- Check the current shell in use:  
  ```bash
  ps -p $$
  ```

- Switch to another shell (e.g., zsh):  
  ```bash
  zsh
  ```

---

## 🌍 Environment

Customize and personalize your shell environment:

- Create an alias:  
  ```bash
  alias ll='ls -la'
  ```

- Customize the terminal prompt (PS1):  
  Example to change color and display directory:  
  ```bash
  export PS1="\[\e[32m\]\w \$ \[\e[0m\]"
  ```

To make changes permanent, add them to your `~/.bashrc`, `~/.zshrc`, or respective shell config file.

---

*Created by Javier Napoles*