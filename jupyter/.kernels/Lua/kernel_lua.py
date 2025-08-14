
from ipykernel.kernelbase import Kernel
import tempfile
import subprocess

class Kernel_Lua(Kernel):
    implementation = 'Kernel_Lua'
    implementation_version = '1.0'
    language = 'lua'
    language_version = '3.8'
    language_info = {
        'name': 'lua',
        'mimetype': 'text/plain',
        'file_extension': '.lua',
    }
    banner = "Kernel-Lua: Execute Lua code in a Jupyter cell."

    # Contant(s)
    cc = 'lua54'

    # API: Code processor.

    def process_code(self, code):
        lua_file = tempfile.NamedTemporaryFile(suffix='.lua', delete=False)
        lua_file.write(code.encode('ascii'))
        lua_file.close()

        exe_res = subprocess.run(' '.join([self.cc, lua_file.name]), shell=True, capture_output=True, text=True)
        if exe_res.returncode == 0:
            result = exe_res.stdout
        else:
            result = exe_res.stderr
            
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
    IPKernelApp.launch_instance(kernel_class=Kernel_Lua)