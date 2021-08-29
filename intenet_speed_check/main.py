'''
Test Internet speed using python
Author: Jayesh Chaudhari
Mail: jayeshchau598007@gmail.com
'''

'''
Install 'pip install speedtest-cli' command in terminal 
'''

import speedtest  # import speedtest command

st = speedtest.Speedtest()

dl = st.download()    # for downlaod speed
ul = st.upload()    # for upload speed

dl = dl/1000000    # converting the bits data speed into Mbps 
ul = ul/1000000    # to convert, divide bits data speed by 10^6(1000000)

#print internet speed
print('Download Speed:', round(dl,2), 'Mbps')    
print('Upload Speed:', round(ul,2), 'Mbps')


# ^^^ rounding the data upto 2 decimals --> round(dl,2)



