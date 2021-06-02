import re
from typing import Text

text_to_search='''

555.222.6584
547 458 6963
475-214-7962

fit decision relate more. Trouble top let common become question. Material challenge food provide. xfletcher@gmail.com 182-88-0121Leg but market audience five factor.8662789809Prepare discover Mrs worry five knowledge test. Always nor control us.
Sound forget very get deep. Similar moment question. hmartin@yahoo.com 345-08-3077Whatever drive necessary bill region after fill.331-361-4901x7075Artist office either game structure address itself thousand. Lose stock process impact wonder watch general. Pass especially development hot citizen western. He eight hospital structure task image raise radio.
Couple let war like. Through pay learn hit require choose official. Continue test dark detail. joelhughes@gmail.com 807-97-4766Would under century skin political project team.844-177-9348Artist sometimes strong inside them news door. Owner prove discover project son. Campaign high huge act camera.
Style dog action want citizen world thus TV. Year she know economic. Before stay partner several try try attention. ortizjames@mora.net 407-93-1998Near thing story bag marriage listen.(398)804-1710Politics offer degree. Agency rest design guess debate wish.
Every today doctor course us. Newspaper positive admit sport. Media whom point decade money later. Art among perform exactly hand. oconnellrobin@yahoo.com 362-81-0177Yeah too personal eye.691.645.7897Serious speak room purpose. What me woman line involve herself.
Young spend discover project some trial. Various need nor. Without over quality set our bad. timothysmith@gmail.com 118-32-6366Indeed production state.624-008-6031State seven two analysis. Eat little almost how you and natural list. Wonder discuss relate writer agree cultural. timothysmith@gmail.com
Total catch great man fly. Such remember production for





'''
#patterns
pattern1='\d{3}.\d{3}.\d{4}'
# phone numbers with missing area code should presume 206
pattern2='\d\d\d.\d\d\d.206\d'
pattern3='Mr\.?\s[A-Z]\w*'
pattern4='M(r|s|rs)\.?\s[A-Z]\w*' #Mr ,Ms Mrs 
pattern5=''
#

pattern=re.compile(r'[a-zA-z0-9.-]\w+@[a-zA-z-]\w+[-_]\w*.(com|edu|net)')
matches=pattern.finditer(text_to_search)

text='''
http://www.raneem.com
https://www.raneem.com
https://raneem.com
https://raneem.gov
http://raneem.gov
'''
pattern=re.compile(r'https?://(www\.)?\w*\.\w*')
matches=pattern.finditer(text)
for match in matches:
        print(match)
with open('assets/potential_contacts.txt','r') as f:
    contacts=f.read()
    
# print(re.sub('[a-z]*@', 'ABC@', s)) s is the text
  
#row string is prefixed with r to not handlign back slashes
# print('\tTab')