
from ipykernel.kernelbase import Kernel
import uuid

class Kernel_C(Kernel):
    implementation = 'Kernel_C'
    implementation_version = '1.0'
    language = 'c'
    language_version = '3.8'
    language_info = {
        'name': 'c',
        'mimetype': 'text/plain',
        'file_extension': '.c',
    }
    banner = "Kernel_C - Execute C code using the GCC toolchain."

    def process_code(self, code):
        result = code.upper()
        return result

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