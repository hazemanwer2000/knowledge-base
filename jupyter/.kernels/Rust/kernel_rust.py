
from ipykernel.kernelbase import Kernel
import tempfile
import subprocess

class Kernel_C(Kernel):
    implementation = 'Kernel_Rust'
    implementation_version = '1.0'
    language = 'rust'
    language_version = '1.56'
    language_info = {
        'name': 'rust',
        'mimetype': 'text/plain',
        'file_extension': '.rs',
    }
    banner = "Kernel-Rust: Execute Rust code in a Jupyter cell."

    # Contant(s)
    cc = 'rustc'

    # API: Code processor.

    def process_code(self, code):
        c_file = tempfile.NamedTemporaryFile(suffix='.rs', delete=False)
        c_file.write(code.encode('ascii'))
        c_file.close()

        exe_file = tempfile.NamedTemporaryFile(suffix='.exe', delete=False)
        exe_file.close()

        cc_argv = [self.cc, '-o', exe_file.name, c_file.name]
        cc_res = subprocess.run(' '.join(cc_argv), shell=True, capture_output=True, text=True)

        if cc_res.returncode == 0:
            exe_res = subprocess.run(exe_file.name, shell=True, capture_output=True, text=True)
            if exe_res.returncode == 0:
                result = exe_res.stdout
            else:
                result = 'Executable was successfully generated, but failed to execute [Error-Code: ' + str(exe_res.returncode) + '].'
        else:
            result = '\n\n'.join(['Toolchain [' + self.cc + '] failed with the following error(s):', ' '.join(cc_argv), cc_res.stderr])
        return result

    # API: Executioner.

    def do_execute(self, code, silent, store_history=True, user_expressions=None, allow_stdin=False):
        result = self.process_code(code)

        self.send_response(self.iopub_socket, 'stream', {'name': 'stdout', 'text': result})

        return {
            'status': 'ok',
            'execution_count': self.execution_count,
            'payload': [],
            'user_expressions': {},
        }
        
if __name__ == '__main__':
    from ipykernel.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=Kernel_C)