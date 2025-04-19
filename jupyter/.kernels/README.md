
## How to create *Jupyter Kernels*?

To create a custom Juypter Kernel,

- Create a directory called `kernel_NAME`, with a `kernel.json` inside, and place it under `jupyter/kernels`.
    - `kernel_NAME` is the name of the kernel (see below).
    - `display_name` is the user-friendly name of the kernel.
    - `language` may identify a programming language, but not compulsory (e.g., `plain text` is allowed).

```
{
 "argv": [
  "python",
  "-m",
  "kernel_NAME",
  "-f",
  "{connection_file}"
 ],
 "display_name": "(...)",
 "language": "LANGUAGE"
}
```

- Create a kernel (i.e., `kernel_NAME.py`) according to the template given, and place it under `site-packages`.