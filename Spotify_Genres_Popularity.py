import pandas as pd
import wordcloud
import json
import csv
from matplotlib import pyplot as plt

dataPath = "./Top50_USA.csv"
df = pd.read_csv(dataPath)
df = df.to_string()
#print(df)

def calculate_frequencies(file_contents): 
    result = {}
    for row in file_contents.iterrows():
        words = row["Artist Genres"]
        print(words)
        #for word in json.loads(words.replace("'", '"')):
        for word in words:
            if word not in result:
                result[word]=1
            else:
                result[word]+=1

    sorted_tuples =sorted(result.items(), key=lambda item:item[1],reverse=True)
    result={k: v for k, v in sorted_tuples}
    with open ("./Pop_genres.csv","w", newline='') as file:
        writer=csv.writer(file)
        writer.writerow(["Genres", "Popularity"])
        for key, value in result.items():
            writer.writerow([key,value])
    
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(result)
    return cloud.to_array()
    
# Display wordcloud image

myimage = calculate_frequencies(df)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()


