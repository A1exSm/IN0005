url = ['https://cam.ac.uk','https://princeton.edu','https://prezi.com','https://en.wikipedia.org','https://pt.wikipedia.org','https://opera.com','https://sec.gov','https://disqus.com','https://oecd.org','https://oecd.org','https://gravatar.com','https://sapo.pt','https://draft.blogger.com','https://mediafire.com','https://bbc.com','https://maps.google.com','https://fb.com','https://metro.co.uk','https://docs.google.com','https://hollywoodreporter.com','https://sites.google.com','https://mediafire.com','https://berkeley.edu','https://nytimes.com','https://sputniknews.com','https://airbnb.com','https://oecd.org','https://ea.com','https://mystrikingly.com','https://fr.wikipedia.org','https://scribd.com','https://cam.ac.uk','https://princeton.edu','https://prezi.com','https://en.wikipedia.org','https://pt.wikipedia.org','https://opera.com','https://sec.gov','https://disqus.com','https://oecd.org','https://oecd.org','https://gravatar.com','https://sapo.pt','https://draft.blogger.com','https://mediafire.com','https://bbc.com','https://maps.google.com','https://fb.com','https://metro.co.uk','https://docs.google.com','https://hollywoodreporter.com','https://sites.google.com','https://mediafire.com','https://berkeley.edu','https://nytimes.com','https://sputniknews.com','https://airbnb.com','https://oecd.org','https://ea.com','https://mystrikingly.com','https://fr.wikipedia.org','https://scribd.com']
#counters for the top 5
top1 = 0
top2 = 0
top3 = 0
top4 = 0
top5 = 0
#list containing the top 5, default values changed when they are identified
rec = ['0','1','2', '3', '4']
n = 0
for link in url:
    #saves the number of occurences of the link in variable temp
    temp = url.count(link)
    #checks whether the value is already in the top5 list
    #if not, it checks whether the number of times it occurs is greater than a top 5
    #if it is it replaces what was in the place previously and updates the count for its top
    if rec.count(link) == 0:
        if temp > top1:
            top1 = temp
            rec[0] = link
            
        elif temp > top2:
            top2 = temp
            rec[1] = link
            
        elif temp > top3:
            top3 = temp
            rec[2] = link

        elif temp > top4:
            top4 = temp
            rec[3] = link

        elif temp > top5:
            top5 = temp
            rec[4] = link

        else:
            continue

    else:
        continue

print(f'Recommended websites: \n1.{rec[0]}\n2.{rec[1]}\n3.{rec[2]}\n4.{rec[3]}\n5.{rec[4]}')
url.append(str(input('Search Bar | ')))
