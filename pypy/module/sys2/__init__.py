from pypy.interpreter.newmodule import ExtModule

class Module(ExtModule):
    """Sys Builtin Module. """
    interpleveldefs = {
        'pypy_objspaceclass'    : '(space.wrap(space.__class__.__name__))', 

        '__name__'              : '(space.wrap("sys"))', 
        '__doc__'               : '(space.wrap("PyPy sys module"))', 

        'platform'              : 'space.wrap(sys.platform)', 
        'maxint'                : 'space.wrap(sys.maxint)', 
        'byteorder'             : 'space.wrap(sys.byteorder)', 
        'exec_prefix'           : 'space.wrap(sys.exec_prefix)', 
        'prefix'                : 'space.wrap(sys.prefix)', 
        'maxunicode'            : 'space.wrap(sys.maxunicode)',
        'maxint'                : 'space.wrap(sys.maxint)',
        'stdin'                 : 'space.wrap(sys.stdin)',
        'stdout'                : 'space.wrap(sys.stdout)',
        'stderr'                : 'space.wrap(sys.stderr)', 
        'pypy_objspaceclass'    : 'space.wrap(space.__class__.__name__)', 

        'path'                  : 'state.get(space).w_path', 
        'modules'               : 'state.get(space).w_modules', 
        'argv'                  : 'state.get(space).w_argv', 
        'warnoptions'           : 'state.get(space).w_warnoptions', 
        'builtin_module_names'  : 'state.get(space).w_builtin_module_names', 
        'pypy_getudir'          : 'state.pypy_getudir', 

        'getdefaultencoding'    : 'space.wrap(sys.getdefaultencoding())', 
        'getrefcount'           : 'vm.getrefcount', 
        '_getframe'             : 'vm._getframe', 
        'setrecursionlimit'     : 'vm.setrecursionlimit', 
        'getrecursionlimit'     : 'vm.getrecursionlimit', 
        'setcheckinterval'      : 'vm.setcheckinterval', 
        'getcheckinterval'      : 'vm.getcheckinterval', 
        'exc_info'              : 'vm.exc_info', 
        'exc_clear'             : 'vm.exc_clear', 

        'executable'            : 'space.wrap("py.py")', 
        'copyright'             : 'space.wrap("MIT-License")', 
        'version_info'          : 'space.wrap((2,3,4, "pypy1"))', 
        'version'               : 'space.wrap("2.3.4 (pypy1 build)")', 
        'hexversion'            : 'space.wrap(0x020304a0)', 
        'ps1'                   : 'space.wrap(">>>>")', 
        'ps2'                   : 'space.wrap("....")', 
    }
    appleveldefs = {
        'displayhook'           : 'app.displayhook', 
        '__displayhook__'       : 'app.__displayhook__', 
        'excepthook'            : 'app.excepthook', 
        '__excepthook__'        : 'app.__excepthook__', 
        'exit'                  : 'app.exit', 
    }

    def getdictvalue(self, space, attr): 
        """ specialize access to dynamic exc_* attributes. """ 
        value = ExtModule.getdictvalue(self, space, attr) 
        if value is not None: 
            return value 
        if attr == 'exc_type':
            operror = space.getexecutioncontext().sys_exc_info()
            if operror is None:
                return space.w_None
            else:
                return operror.w_type
        elif attr == 'exc_value':
            operror = space.getexecutioncontext().sys_exc_info()
            if operror is None:
                return space.w_None
            else:
                return operror.w_value
        elif attr == 'exc_traceback':
            operror = space.getexecutioncontext().sys_exc_info()
            if operror is None:
                return space.w_None
            else:
                return space.wrap(operror.application_traceback)
        return None 
