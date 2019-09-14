import unittest
from unittest import mock
from tests.recipes.recipe_lib_test import BaseTestForCmakeRecipe


class TestOpenalRecipe(BaseTestForCmakeRecipe, unittest.TestCase):
    """
    An unittest for recipe :mod:`~pythonforandroid.recipes.openal`
    """
    recipe_name = "openal"

    @mock.patch("pythonforandroid.recipes.openal.sh.cmake")
    @mock.patch("pythonforandroid.recipes.openal.sh.make")
    @mock.patch("pythonforandroid.recipes.openal.sh.cp")
    @mock.patch("pythonforandroid.util.chdir")
    @mock.patch("pythonforandroid.build.ensure_dir")
    @mock.patch("pythonforandroid.archs.glob")
    @mock.patch("pythonforandroid.archs.find_executable")
    def test_prebuild_arch(
        self,
        mock_find_executable,
        mock_glob,
        mock_ensure_dir,
        mock_current_directory,
        mock_sh_cp,
        mock_sh_make,
        mock_sh_cmake,
    ):
        mock_find_executable.return_value = (
            "/opt/android/android-ndk/toolchains/"
            "llvm/prebuilt/linux-x86_64/bin/clang"
        )
        mock_glob.return_value = ["llvm"]
        self.recipe.build_arch(self.arch)

        # make sure that the mocked methods are actually called
        mock_glob.assert_called()
        mock_ensure_dir.assert_called()
        mock_current_directory.assert_called()
        mock_find_executable.assert_called()
        mock_sh_cp.assert_called()
        mock_sh_make.assert_called()
        mock_sh_cmake.assert_called()

    @mock.patch("pythonforandroid.recipes.openal.sh.cp")
    @mock.patch("pythonforandroid.util.chdir")
    @mock.patch("pythonforandroid.build.ensure_dir")
    @mock.patch("pythonforandroid.archs.glob")
    @mock.patch("pythonforandroid.archs.find_executable")
    def test_build_arch(
        self,
        mock_find_executable,
        mock_glob,
        mock_ensure_dir,
        mock_current_directory,
        mock_sh_cp,
    ):
        # We overwrite the base test method because we need to mock a little
        # more with this recipe (`sh.cp` and `sh.rm`)
        super().test_build_arch()
        # make sure that the mocked methods are actually called
        mock_sh_cp.assert_called()
