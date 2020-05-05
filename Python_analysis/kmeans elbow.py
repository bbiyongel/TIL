from scipy.spatial.distance import cdist
distortions = []
K = range(1,10)
for k in K:
    kmeanModel = KMeans(n_clusters=k).fit(Z)
    kmeanModel.fit(Z)
    distortions.append(sum(np.min(cdist(Z, kmeanModel.cluster_centers_, 'euclidean'), axis=1)) / Z.shape[0])
# Plot the elbow
plt.plot(K, distortions, 'bx-')
plt.xlabel('k')
plt.ylabel('Distortion')
plt.title('The Elbow Method showing the optimal k')
plt.show()

####################
df = pd.DataFrame(Z)
df['category'] = km.labels_
colormap = { 0: 'red', 1: 'green', 2: 'blue'}
colors = results.apply(lambda row: colormap[row.category], axis=1)
ax = results.plot(kind='scatter', x=0, y=1, alpha=0.1, s=300, c=colors)


https://medium.com/@nsh235482/k-means-clustering-6ab85a2a32ad


# 실루엣, t-sne
https://mkjjo.github.io/finance/2019/01/09/kmeans_corp.html
http://blog.naver.com/PostView.nhn?blogId=samsjang&logNo=221017639342&categoryNo=0&parentCategoryNo=49&viewDate=&currentPage=1&postListTopCurrentPage=1&from=search

#파이썬 중급자 책
https://winterj.me/python-books-for-intermediate/
