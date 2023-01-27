# Imperia_sumok_Page_Object
Auto tests for ImperiaSumok with Page_Object pattern
----------------------------------------------
Console command to launch tests: 
pytest -s -v --browser_name=chrome --reruns 1
To install requirements use command: 'pip3 install -r requirements.txt'
----------------------------------------------

base_page.py - Здесь хранятся методы, которые применяются ко всему проекту.

locators.py - Здесь объявляются локаторы, в виде констант. Локаторы каждой отдельной страницы завёрнуты в класс, чтобы было удобно импортировать.

main_page.py, login_page.py, section_page.py - В этих файлах хранятся методы по конкретным страницам, завернутые в класс этой страницы. 

test_main_page.py, test_login_page.py, test_section_page.py - В этих файлах описаны сами тесты, выполняются методы конкретных страниц.
        
    
