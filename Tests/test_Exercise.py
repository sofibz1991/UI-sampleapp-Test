from Pages.SampleAppPage import SampleAppPage
import pytest

class TestCase():
#1 user_bien, pass_bien, "welcome, user_bien!"
#2 vacio, pass_bien, "invalid username/password"
#3 user_bien, pass_mal, "invalid username/password"
#4 vacio, vacio, "invalid username/password"
#5 vacio, pass_mal, "invalid username/password"
#6 user_bien, vacio, "invalid username/password"
    @pytest.mark.parametrize('user, psw, expected_banner', [('user_bien', 'pwd', 'Welcome, user_bien!'),('', 'pwd', 'Invalid username/password'),('user_bien', 'pwa', 'Invalid username/password'), ('','', 'Invalid username/password'), ('', 'pwd', 'Invalid username/password'), ('user_bien', '', 'Invalid username/password')])
    def test_banner_change(self, init_driver, user, psw, expected_banner):
        self.sampleAppPage = SampleAppPage(init_driver)
        self.sampleAppPage.go_to_SampleApp2()
        #hacer input en usuario
        #hacer input en password
        #hacer click en el botón
        #hacer assertion en el banner
        text_banner = self.sampleAppPage.do_exercise (user, psw)
        print(text_banner)
        assert text_banner == expected_banner
        


#TESTS