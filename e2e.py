from selenium import webdriver

WEBDRIVE_PATH = "./chromedriver.exe"


# This function tests the score written in the MainScore flask server
def test_scores_service(app_url):
    try:
        driver = webdriver.Chrome(executable_path=WEBDRIVE_PATH)
        driver.get(app_url)
        score = driver.find_element_by_id("score").text
    except Exception as e:
        print(e)
    score_as_int = int(score)
    if score_as_int >= 0  and score_as_int <= 1000:
        return 0
    else:
        return 1


if __name__ == '__main__':
    exit(test_scores_service("http://192.168.99.100:8777"))