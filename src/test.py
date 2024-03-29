
import requests

text = "이 이미지의 키워드와 텍스트의 내용을 다음과 같은 형식으로 만들어 주세요 keyword: 키워드, text: 텍스트"
image_url = "https://social-phinf.pstatic.net//20240221_104/1708522564410F1EpB_GIF/image_%281%29.gif"

payload =  {"model": "gpt-4-vision-preview",
    "messages": [
     {"role": "system",
      "content": [{"type": "text",
                   "text": "You are a cool image analyst.  Your goal is to describe what is in this image in korean."}],
     },
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": text 
          },
          {
            "type": "image_url",
            "image_url": {
              "url": image_url
            }
          }
        ]
      }
    ],
    "max_tokens": 4096
  }



headers = {"Authorization": f"Bearer ",
            "Content-Type": "application/json"}


response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=payload)
r = response.json()
print(r)
print(r["choices"][0]["message"]["content"])

import math

math.comb(12, 3)
1001 - 220 - 286

math.factorial(6) - math.factorial(5)
math.factorial(3) * math.factorial(4) * math.factorial(3) * math.factorial(3)
math.comb(2,2) * math.comb(8,1) * math.factorial(3)

720 - 48

math.comb(8,1) + math.comb(8, 3)

64 * math.factorial(3)

20*18*16*14*12*10 / math.factorial(6)

2 * math.comb(10, 6)

math.comb(8,4) * math.comb(7,2) + math.comb(8,3) * math.comb(7,3)