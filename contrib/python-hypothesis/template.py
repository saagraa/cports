pkgname = "python-hypothesis"
pkgver = "6.108.5"
pkgrel = 0
build_wrksrc = "hypothesis-python"
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python-attrs", "python-sortedcontainers"]
checkdepends = [
    "python-black",
    "python-click",
    "python-dateutil",
    "python-pexpect",
    "python-ptyprocess",
    "python-pytest",
    "python-pytest-xdist",
    "python-pytz",
    "python-typing_extensions",
    *depends,
]
pkgdesc = "Python library for property-based testing"
maintainer = "Duncan Bellamy <dunk@denkimushi.com>"
license = "MPL-2.0"
url = "https://hypothesis.works/index.html"
source = f"https://github.com/HypothesisWorks/hypothesis/archive/refs/tags/hypothesis-python-{pkgver}.tar.gz"
sha256 = "bfef44061132d4b07c664d99e94ab83abb06b5b4cec330573dbe9c6e91fb8c24"


def init_check(self):
    self.make_check_args = [
        "--ignore=tests/array_api",
        "--ignore=tests/datetime/test_dateutil_timezones.py",
        "--ignore=tests/dpcontracts/test_contracts.py",
        "--ignore=tests/patching/test_patching.py",
        "--ignore=tests/conjecture/test_utils.py",
        "--ignore=tests/ghostwriter/test_expected_output.py",
        "--ignore=tests/codemods/test_codemods.py",
        "--ignore=tests/lark/test_grammar.py",
        "--ignore=tests/redis/test_redis_exampledatabase.py",
        "--ignore=examples/example_hypothesis_entrypoint/test_entrypoint.py",
        "--ignore=tests/codemods/test_codemod_cli.py",
        "--ignore=tests/pandas",
        "--ignore=tests/numpy",
        "-k",
        # XXX: fails because posix/ tzdata folder doesn't exist
        "not test_can_generate_prefixes_if_allowed_and_available",
        f"--numprocesses={self.make_jobs}",
        "--dist=worksteal",
    ]
