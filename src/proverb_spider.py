import scrapy
import re

class ProverbSpider(scrapy.Spider):
    name = "chinese_proverbs"
    start_urls = [
        "https://www.chinahighlights.com/travelguide/learning-chinese/chinese-sayings.htm",
    ]

    def parse(self, response):
        # Select all potential proverb starters
        proverbs = response.xpath('//p[strong]')
        
        for p in proverbs:
            strong_text = p.xpath('normalize-space(strong/text())').get()
            if not (strong_text and re.match(r'^\d+\.', strong_text)):
                continue

            # Chinese text
            chinese = re.sub(r'\s*\(.*?\)', '', strong_text).strip()

            # English translation
            eng_p = p.xpath('./following-sibling::p[1]')
            english = eng_p.xpath('normalize-space()').get()
            english = re.sub(r'^—\s*', '', english) if english else ''

            # Origin collection
            origin = []
            current_node = p.xpath('./following-sibling::p[2]')
            
            while current_node:
                # Check for next proverb or section header
                if current_node.xpath('./strong[contains(translate(substring(normalize-space(), 1, 1), "1234567890", ""), "")]') or current_node.xpath('self::h2'):
                    break
                
                # Get clean text and move to next
                text = current_node.xpath('normalize-space()').get()
                if text:
                    origin.append(text)
                current_node = current_node.xpath('./following-sibling::p[1]')

            yield {
                "chinese": chinese,
                "english": english,
                "origin": " ".join(origin) if origin else None
            }