pkgname = "mygui"
pkgver = "3.4.3"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DMYGUI_BUILD_DEMOS=OFF",
    "-DMYGUI_BUILD_TOOLS=OFF",
    "-DMYGUI_RENDERSYSTEM=1",
]
hostmakedepends = ["cmake", "ninja", "pkgconf", "doxygen"]
makedepends = [
    "libx11-devel",
    "boost-devel",
    "freetype-devel",
    "sdl-devel",
    "mesa-devel",
    "zlib-devel",
]
pkgdesc = "Fast, flexible and simple GUI"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/MyGUI"
source = f"{url}/{pkgname}/archive/MyGUI{pkgver}.tar.gz"
sha256 = "33c91b531993047e77cace36d6fea73634b8c17bd0ed193d4cd12ac7c6328abd"
# unit tests are off
options = ["!check"]


def post_install(self):
    self.install_license("COPYING.MIT")


@subpackage("mygui-devel")
def _devel(self):
    return self.default_devel()
