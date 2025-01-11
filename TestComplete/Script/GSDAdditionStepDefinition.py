"""GSDAdditionWorkFlow"""
from GSDAdditionWorkFlow import GSDAdditionWorkFlow
import CommonUtil
import Operationclientutility
import Applicationutility
import GSDAdditionutility

obj=GSDAdditionWorkFlow()

@when("I click the {arg} button in the GSD Addition Window")
def step_impl(button):
    """I click the '<button>' button in the GSD Addition Window"""
    CommonUtil.write_text_file(f"\nWhen I click the '{button}' button in the GSD Addition Window")
    Applicationutility.wait_in_seconds(6000, "wait")
    obj.clickbuttoningsdwindow(button)
    
@when("I click the {arg} button in the GSD Additions Window")
def step_impl(button):
    """I click the '<button>' button in the GSD Additions Window"""
    CommonUtil.write_text_file(f"\nWhen I click the '{button}' button in the GSD Additions Window")
    Applicationutility.wait_in_seconds(2000, "wait")
    obj.clickbuttoningsdwindow(button)
    Applicationutility.wait_in_seconds(80000, "wait")
    
@when("I select {arg} in the GSD Browser")
def step_impl(folder):
    """I select '<folder>' in the GSD Browser"""
    CommonUtil.write_text_file(f"\nWhen I select '{folder}' in the GSD Browser")
    obj.selectfolderingsdwindow(folder)
    
@when("I click the {arg} button in duplicate file window")
def step_impl(button):
    """I click the "<button>" button in duplicate file window"""
    CommonUtil.write_text_file(f"\nWhen I click the '{button}' button in duplicate file window")
    obj.handleduplicatefileingsdwindow(button)
    
@when("I select the {arg} in delete device library window")
def step_impl(file_name):
    """I select the '<file_name>' in delete device library window"""
    CommonUtil.write_text_file(f"\nWhen I select the '{file_name}' in delete device library window")
    obj.deletefileingsdwindow(file_name)
    
@when("I click {arg} button in delete device library window")
def step_impl(button):
    """I click '<button>' button in delete device library window"""
    CommonUtil.write_text_file(f"\nWhen I click '{button}' button in delete device library window")
    obj.clickbuttoningsddeletewindow(button)
    
@when("I click {arg} button in delete device library popup window")
def step_impl(button):
    """I click '<button>' button in delete device library popup window"""
    CommonUtil.write_text_file(f"\nWhen I click '{button}' button in delete device library popup window")
    obj.clickbuttoningsddeletepopupwindow(button)