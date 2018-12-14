import re
pattern = r'\[[^\]]*\] '
pattern2 = r'\[[^\]]*\]'
with open ('sponjibobu.txt', 'r') as with_bracket:
    content = with_bracket.read()
content_new = re.sub(pattern, '', content)
content_new = re.sub(pattern2, '', content_new)

withoutbracket = open('sponjibobu.txt', 'w')
withoutbracket.write(content_new)
