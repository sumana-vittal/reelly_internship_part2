from selenium.webdriver.common.by import By

from pages.base_page import Page


class UserGuidePage(Page):

   VIDEO_TITLE = (By.CSS_SELECTOR, "a.ytp-title-link.yt-uix-sessionlink")
   IFRAME1 = (By.CSS_SELECTOR, "div.video-2.w-video.w-embed iframe.embedly-embed")
   IFRAME2 = (By.CSS_SELECTOR, "#player")

   def verify_user_guide_opens(self):
      self.verify_partial_url("user-guide")

   def verify_video_titles(self):

      #switch the frames
      self.switch_frames(*self.IFRAME1)

      self.switch_frames(*self.IFRAME2)

      #get all titles
      video_titles = self.driver.find_elements(*self.VIDEO_TITLE)
      print(len(video_titles))
      for title in video_titles:
         print(title.text)
         self.presence_of_element_located(*self.VIDEO_TITLE)

      #switch back to default.
      self.reset_frame()