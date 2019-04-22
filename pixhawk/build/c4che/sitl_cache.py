AP_LIBRARIES = ['AP_HAL_SITL', 'SITL']
AP_LIBRARIES_OBJECTS_KW = {}
AR = ['/usr/bin/ar']
ARFLAGS = ['rcs']
BINDIR = '/usr/bin'
BOARD = 'sitl'
BOOTLOADER = False
BUILD_SUMMARY_HEADER = ['target', 'size_text', 'size_data', 'size_bss', 'size_total']
CC = ['/usr/bin/gcc']
CCLNK_SRC_F = []
CCLNK_TGT_F = ['-o']
CC_NAME = 'gcc'
CC_SRC_F = []
CC_TGT_F = ['-c', '-o']
CC_VERSION = ('5', '4', '0')
CFLAGS = ['-ffunction-sections', '-fdata-sections', '-fsigned-char', '-Wall', '-Wextra', '-Wformat', '-Wpointer-arith', '-Wcast-align', '-Wundef', '-Wno-missing-field-initializers', '-Wno-unused-parameter', '-Wno-redundant-decls', '-Wno-unknown-pragmas', '-Wno-trigraphs', '-Werror=shadow', '-Werror=return-type', '-Werror=unused-result', '-Werror=narrowing', '-Werror=attributes', '-MMD']
CFLAGS_MACBUNDLE = ['-fPIC']
CFLAGS_cshlib = ['-fPIC']
COMPILER_CC = 'gcc'
COMPILER_CXX = 'g++'
CONFIGURE_FILES = ['/home/haggisaerospace/ardupilot/ardupilot/modules/waf/waflib/Tools/compiler_cxx.py', '/usr/lib/python3.5/linecache.py', '/usr/lib/python3.5/collections/abc.py', '/usr/lib/python3.5/_sysconfigdata.py', '/usr/lib/python3.5/copyreg.py', '/usr/lib/python3.5/shlex.py', '/usr/lib/python3.5/optparse.py', '/home/haggisaerospace/ardupilot/ardupilot/modules/waf/waflib/Options.py', '/usr/lib/python3.5/encodings/utf_8.py', 'Tools/ardupilotwaf/toolchain.py', '/usr/lib/python3.5/hashlib.py', '/usr/lib/python3.5/gettext.py', 'Tools/ardupilotwaf/git_submodule.py', '/usr/lib/python3.5/ast.py', '/usr/lib/python3.5/_compression.py', 'Tools/ardupilotwaf/build_summary.py', '/usr/lib/python3.5/encodings/__init__.py', 'Tools/ardupilotwaf/uavcangen.py', '/usr/lib/python3.5/posixpath.py', 'Tools/ardupilotwaf/boards.py', '/usr/lib/python3.5/fnmatch.py', '/home/haggisaerospace/ardupilot/ardupilot/modules/waf/waflib/Tools/c_osx.py', '/usr/lib/python3.5/weakref.py', '/home/haggisaerospace/ardupilot/ardupilot/modules/waf/waflib/Node.py', '/home/haggisaerospace/ardupilot/ardupilot/modules/waf/waflib/Task.py', '/usr/lib/python3.5/json/scanner.py', '/usr/lib/python3.5/json/encoder.py', '/home/haggisaerospace/ardupilot/ardupilot/modules/waf/waflib/extras/c_bgxlc.py', '/usr/lib/python3.5/json/decoder.py', '/home/haggisaerospace/ardupilot/ardupilot/modules/waf/waflib/Tools/c_tests.py', '/usr/lib/python3.5/lib-dynload/_bz2.cpython-35m-x86_64-linux-gnu.so', '/home/haggisaerospace/ardupilot/ardupilot/modules/waf/waflib/extras/c_emscripten.py', '/usr/lib/python3.5/signal.py', '/usr/lib/python3.5/keyword.py', '/usr/lib/python3.5/platform.py', '/home/haggisaerospace/ardupilot/ardupilot/modules/waf/waflib/__init__.py', '/usr/lib/python3.5/importlib/__init__.py', '/usr/lib/python3.5/io.py', '/home/haggisaerospace/ardupilot/ardupilot/modules/waf/waflib/Logs.py', '/usr/lib/python3.5/functools.py', '/home/haggisaerospace/ardupilot/ardupilot/modules/waf/waflib/extras/__init__.py', '/usr/lib/python3.5/subprocess.py', '/usr/lib/python3.5/datetime.py', '/home/haggisaerospace/ardupilot/ardupilot/modules/waf/waflib/Tools/python.py', '/usr/lib/python3.5/encodings/hex_codec.py', '/home/haggisaerospace/ardupilot/ardupilot/modules/waf/waflib/Tools/__init__.py', '/usr/lib/python3.5/lib-dynload/termios.cpython-35m-x86_64-linux-gnu.so', '/home/haggisaerospace/ardupilot/ardupilot/modules/waf/waflib/Tools/c_aliases.py', '/home/haggisaerospace/ardupilot/ardupilot/modules/waf/waf-light', '/usr/lib/python3.5/pipes.py', '/usr/lib/python3.5/importlib/machinery.py', '/usr/lib/python3.5/locale.py', '/usr/lib/python3.5/traceback.py', '/usr/lib/python3.5/queue.py', '/usr/lib/python3.5/sre_compile.py', 'Tools/ardupilotwaf/ap_library.py', '/home/haggisaerospace/ardupilot/ardupilot/modules/waf/waflib/Tools/gcc.py', '/home/haggisaerospace/ardupilot/ardupilot/modules/waf/waflib/Tools/ccroot.py', '/home/haggisaerospace/ardupilot/ardupilot/modules/waf/waflib/Tools/c.py', 'Tools/ardupilotwaf/ap_persistent.py', '/home/haggisaerospace/ardupilot/ardupilot/modules/waf/waflib/Tools/ar.py', '/usr/lib/python3.5/lzma.py', '/usr/lib/python3.5/sitecustomize.py', '/usr/lib/python3.5/lib-dynload/_lzma.cpython-35m-x86_64-linux-gnu.so', '/usr/lib/python3.5/sre_parse.py', '/usr/lib/python3.5/threading.py', '/usr/lib/python3.5/ctypes/__init__.py', '/usr/lib/python3.5/token.py', '/usr/lib/python3.5/importlib/abc.py', '/home/haggisaerospace/ardupilot/ardupilot/modules/waf/waflib/extras/clang_compilation_database.py', '/usr/lib/python3.5/_bootlocale.py', '/usr/lib/python3.5/lib-dynload/_opcode.cpython-35m-x86_64-linux-gnu.so', 'Tools/ardupilotwaf/cxx_checks.py', '/usr/lib/python3.5/types.py', '/usr/lib/python3.5/lib-dynload/_ctypes.cpython-35m-x86_64-linux-gnu.so', '/usr/lib/python3.5/dis.py', '/usr/lib/python3.5/struct.py', '/usr/lib/python3.5/string.py', '/usr/lib/python3.5/operator.py', '/usr/lib/python3.5/sysconfig.py', '/usr/lib/python3.5/importlib/util.py', '/home/haggisaerospace/ardupilot/ardupilot/modules/waf/waflib/Utils.py', '/usr/lib/python3.5/warnings.py', '/home/haggisaerospace/ardupilot/ardupilot/modules/waf/waflib/Tools/cxx.py', 'Tools/ardupilotwaf/gtest.py', '/usr/lib/python3.5/enum.py', '/usr/lib/python3.5/random.py', '/home/haggisaerospace/ardupilot/ardupilot/modules/waf/waflib/Context.py', '/home/haggisaerospace/ardupilot/ardupilot/modules/waf/waflib/Errors.py', '/usr/lib/python3.5/bz2.py', '/home/haggisaerospace/ardupilot/ardupilot/modules/waf/waflib/Tools/compiler_c.py', '/usr/lib/python3.5/base64.py', '/usr/lib/python3.5/importlib/_bootstrap_external.py', '/usr/lib/python3.5/collections/__init__.py', '/usr/lib/python3.5/reprlib.py', '/usr/lib/python3.5/_sitebuiltins.py', '/usr/lib/python3.5/stat.py', '/usr/lib/python3.5/importlib/_bootstrap.py', '/usr/lib/python3.5/sre_constants.py', '/home/haggisaerospace/ardupilot/ardupilot/modules/waf/waflib/Runner.py', '/usr/lib/python3.5/heapq.py', '/usr/lib/python3.5/imp.py', '/home/haggisaerospace/ardupilot/ardupilot/modules/waf/waflib/Tools/icc.py', '/home/haggisaerospace/ardupilot/ardupilot/modules/waf/waflib/extras/c_nec.py', '/usr/lib/python3.5/_compat_pickle.py', 'Tools/ardupilotwaf/mavgen.py', '/usr/lib/python3.5/inspect.py', '/usr/lib/python3.5/_collections_abc.py', '/usr/lib/python3.5/copy.py', '/usr/lib/python3.5/plat-x86_64-linux-gnu/_sysconfigdata_m.py', '/home/haggisaerospace/ardupilot/ardupilot/modules/waf/waflib/Tools/gxx.py', '/usr/lib/python3.5/lib-dynload/_json.cpython-35m-x86_64-linux-gnu.so', '/home/haggisaerospace/ardupilot/ardupilot/modules/waf/waflib/TaskGen.py', '/home/haggisaerospace/ardupilot/ardupilot/modules/waf/waflib/Tools/waf_unit_test.py', '/usr/lib/python3.5/xml/etree/ElementPath.py', '/usr/lib/python3.5/xml/etree/__init__.py', '/usr/lib/python3.5/xml/__init__.py', '/usr/lib/python3.5/opcode.py', '/home/haggisaerospace/ardupilot/ardupilot/modules/waf/waflib/extras/gccdeps.py', '/usr/lib/python3.5/os.py', '/home/haggisaerospace/ardupilot/ardupilot/modules/waf/waflib/Scripting.py', '/usr/lib/python3.5/__future__.py', '/home/haggisaerospace/ardupilot/ardupilot/modules/waf/waflib/Tools/c_config.py', 'Tools/ardupilotwaf/static_linking.py', '/usr/lib/python3.5/textwrap.py', '/usr/lib/python3.5/re.py', '/home/haggisaerospace/ardupilot/ardupilot/modules/waf/waflib/Tools/clang.py', '/usr/lib/python3.5/lib-dynload/_hashlib.cpython-35m-x86_64-linux-gnu.so', '/usr/lib/python3.5/tempfile.py', '/usr/lib/python3.5/contextlib.py', '/usr/lib/python3.5/tarfile.py', '/home/haggisaerospace/ardupilot/ardupilot/modules/waf/waflib/Build.py', '/home/haggisaerospace/ardupilot/ardupilot/modules/waf/waflib/Tools/clangxx.py', '/home/haggisaerospace/ardupilot/ardupilot/modules/waf/waflib/Tools/icpc.py', '/home/haggisaerospace/ardupilot/ardupilot/modules/waf/waflib/Configure.py', '/usr/lib/python3.5/_weakrefset.py', '/usr/lib/python3/dist-packages/apport_python_hook.py', '/usr/lib/python3.5/encodings/latin_1.py', '/usr/lib/python3.5/selectors.py', '/usr/lib/python3.5/encodings/aliases.py', '/home/haggisaerospace/ardupilot/ardupilot/modules/waf/waflib/Tools/xlc.py', '/usr/lib/python3.5/site.py', '/usr/lib/python3.5/shutil.py', 'Tools/ardupilotwaf/ardupilotwaf.py', '/home/haggisaerospace/ardupilot/ardupilot/modules/waf/waflib/Tools/c_preproc.py', '/usr/lib/python3.5/logging/__init__.py', '/usr/lib/python3.5/genericpath.py', '/usr/lib/python3.5/tokenize.py', '/usr/lib/python3.5/xml/etree/ElementTree.py', '/usr/lib/python3.5/json/__init__.py', '/usr/lib/python3.5/abc.py', '/home/haggisaerospace/ardupilot/ardupilot/modules/waf/waflib/ConfigSet.py', '/usr/lib/python3.5/codecs.py', '/usr/lib/python3.5/ctypes/_endian.py', '/usr/lib/python3.5/pickle.py', '/home/haggisaerospace/ardupilot/ardupilot/modules/waf/waflib/ansiterm.py', '/home/haggisaerospace/ardupilot/ardupilot/wscript']
CONFIGURE_HASH = b'\xfb\x06\xe6Q7\xea\x9c\xa2`\xd6\xa9\x91Iw]\xc0'
CPPPATH_ST = '-I%s'
CXX = ['/usr/bin/g++']
CXXFLAGS = ['-std=gnu++11', '-fdata-sections', '-ffunction-sections', '-fno-exceptions', '-fsigned-char', '-Wall', '-Wextra', '-Wformat', '-Wpointer-arith', '-Wcast-align', '-Wundef', '-Wno-unused-parameter', '-Wno-missing-field-initializers', '-Wno-reorder', '-Wno-redundant-decls', '-Wno-unknown-pragmas', '-Werror=attributes', '-Werror=format-security', '-Werror=enum-compare', '-Werror=array-bounds', '-Werror=uninitialized', '-Werror=init-self', '-Werror=narrowing', '-Werror=return-type', '-Werror=switch', '-Werror=sign-compare', '-Werror=type-limits', '-Werror=unused-result', '-Werror=shadow', '-Werror=unused-variable', '-Wfatal-errors', '-Wno-trigraphs', '-Werror=unused-but-set-variable', '-Werror=float-equal', '-O3', '-MMD']
CXXFLAGS_MACBUNDLE = ['-fPIC']
CXXFLAGS_cxxshlib = ['-fPIC']
CXXLNK_SRC_F = []
CXXLNK_TGT_F = ['-o']
CXX_NAME = 'gcc'
CXX_SRC_F = []
CXX_TGT_F = ['-c', '-o']
DEBUG = False
DEFINES = ['SKETCHBOOK="/home/haggisaerospace/ardupilot/ardupilot"', 'AP_SCRIPTING_CHECKS=1', 'CONFIG_HAL_BOARD=HAL_BOARD_SITL', 'CONFIG_HAL_BOARD_SUBTYPE=HAL_BOARD_SUBTYPE_NONE']
DEFINES_ST = '-D%s'
DEFINE_COMMENTS = {'__STDC_FORMAT_MACROS': '', 'NEED_CMATH_ISFINITE_STD_NAMESPACE': '', 'HAVE_BYTESWAP_H': '', 'PYTHONDIR': '', 'NEED_CMATH_ISINF_STD_NAMESPACE': '', 'WAF_BUILD': '', 'HAVE_CMATH_ISINF': '', 'HAVE_ENDIAN_H': '', 'HAVE_CMATH_ISFINITE': '', 'PYTHONARCHDIR': '', 'HAVE_MEMRCHR': '', '_GNU_SOURCE': '', 'NEED_CMATH_ISNAN_STD_NAMESPACE': '', 'HAVE_CMATH_ISNAN': ''}
DEST_BINFMT = 'elf'
DEST_CPU = 'x86_64'
DEST_OS = 'linux'
DSDL_COMPILER = '/home/haggisaerospace/ardupilot/ardupilot/modules/uavcan/libuavcan/dsdl_compiler/libuavcan_dsdlc'
DSDL_COMPILER_DIR = '/home/haggisaerospace/ardupilot/ardupilot/modules/uavcan/libuavcan/dsdl_compiler'
ENABLE_ASSERTS = False
ENABLE_GCCDEPS = ['c', 'cxx']
ENABLE_HEADER_CHECKS = False
GIT = ['/usr/bin/git']
GIT_SUBMODULES = ['gtest', 'mavlink']
HAS_GTEST = True
HAVE_BYTESWAP_H = 1
HAVE_CMATH_ISFINITE = 1
HAVE_CMATH_ISINF = 1
HAVE_CMATH_ISNAN = 1
HAVE_ENDIAN_H = 1
HAVE_MEMRCHR = 1
INCLUDES = ['/home/haggisaerospace/ardupilot/ardupilot/libraries/', '/home/haggisaerospace/ardupilot/ardupilot/libraries/AP_Common/missing']
LIB = ['m']
LIBDIR = '/usr/lib'
LIBPATH_ST = '-L%s'
LIB_ST = '-l%s'
LINKFLAGS = ['-Wl,--gc-sections', '-pthread']
LINKFLAGS_MACBUNDLE = ['-bundle', '-undefined', 'dynamic_lookup']
LINKFLAGS_cshlib = ['-shared']
LINKFLAGS_cstlib = ['-Wl,-Bstatic']
LINKFLAGS_cxxshlib = ['-shared']
LINKFLAGS_cxxstlib = ['-Wl,-Bstatic']
LINK_CC = ['/usr/bin/gcc']
LINK_CXX = ['/usr/bin/g++']
MAVLINK_DIR = '/home/haggisaerospace/ardupilot/ardupilot/modules/mavlink'
NEED_CMATH_ISFINITE_STD_NAMESPACE = 1
NEED_CMATH_ISINF_STD_NAMESPACE = 1
NEED_CMATH_ISNAN_STD_NAMESPACE = 1
OPTIONS = {'prefix': '/usr', 'sitl_flash_storage': False, 'dump_test_scripts': False, 'keep': 0, 'enable_asserts': False, 'check_verbose': None, 'bindir': None, 'enable_math_check_indexes': False, 'apstatedir': '', 'pythondir': None, 'no_lock_in_top': '', 'enable_sfml': False, 'program_group': [], 'python': None, 'top': '', 'enable_sfml_audio': False, 'rsync_dest': '', 'distcheck_args': None, 'jobs': 8, 'default_parameters': None, 'no_tests': False, 'scripting_checks': True, 'colors': 'auto', 'no_lock_in_out': '', 'testcmd': False, 'upload': None, 'enable_scripting': False, 'check_c_compiler': None, 'toolchain': None, 'bootloader': False, 'clean_all_sigs': None, 'enable_lttng': False, 'targets': '', 'no_lock_in_run': '', 'disable_gccdeps': False, 'clear_failed_tests': False, 'progress_bar': 0, 'out': '', 'libdir': None, 'pdb': 0, 'autoconfig': True, 'enable_header_checks': False, 'submodule_update': True, 'whelp': 0, 'profile': 0, 'lcov_report': False, 'pyc': 1, 'summary_all': None, 'zones': '', 'force': False, 'use_nuttx_iofw': False, 'static': False, 'check_cxx_compiler': None, 'enable_gcov': False, 'all_tests': False, 'board': 'sitl', 'pyo': 1, 'debug': False, 'disable_tests': False, 'disable_libiio': False, 'verbose': 0, 'destdir': '', 'files': '', 'pythonarchdir': None, 'nopycache': None, 'enable_benchmarks': False}
PREFIX = '/usr'
PYC = 1
PYFLAGS = ''
PYFLAGS_OPT = '-O'
PYO = 1
PYTAG = 'cpython-35'
PYTHON = ['/usr/bin/python3']
PYTHONARCHDIR = '/usr/lib/python3/dist-packages'
PYTHONDIR = '/usr/lib/python3/dist-packages'
PYTHON_VERSION = '3.5'
ROMFS_FILES = []
RPATH_ST = '-Wl,-rpath,%s'
RSYNC = ['/usr/bin/rsync']
SHLIB_MARKER = '-Wl,-Bdynamic'
SIZE = ['/usr/bin/size']
SONAME_ST = '-Wl,-h,%s'
STLIBPATH_ST = '-L%s'
STLIB_MARKER = '-Wl,-Bstatic'
STLIB_ST = '-l%s'
SUBMODULE_UPDATE = True
TOOLCHAIN = 'native'
USE_NUTTX_IOFW = False
cfg_files = ['/home/haggisaerospace/ardupilot/ardupilot/build/sitl/ap_config.h']
cprogram_PATTERN = '%s'
cshlib_PATTERN = 'lib%s.so'
cstlib_PATTERN = 'lib%s.a'
cxxprogram_PATTERN = '%s'
cxxshlib_PATTERN = 'lib%s.so'
cxxstlib_PATTERN = 'lib%s.a'
define_key = []
macbundle_PATTERN = '%s.bundle'
