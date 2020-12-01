import numpy as np
import uuid
from matplotlib import pyplot as plt

class cat:
    def __init__(self, year_born):
        self.id = str(uuid.uuid4())
        self.year_born = year_born
        self.lifespan = self.get_cat_lifespan()
        self.year_died = self.year_born + self.lifespan

    def get_cat_lifespan(self):
        mu, sigma = 15, 4
        lifetime = np.random.normal(mu, sigma)
        return int(round(lifetime))

    def cat_alive(self, year_now):
        if (year_now <= (self.year_born + self.lifespan)):
            return True
        else:
            return False

def simulate():
    cats = []
    alive_cats = set([])
    year_data = []
    for year in range(2014,2100,1):
        if ((year-2014)%5 == 0):
            cats.append(cat(year))
            cats.append(cat(year))
        for c in cats:
            if c.cat_alive(year):
                alive_cats.add(c.id)
            else:
                try:
                    alive_cats.remove(c.id)
                except:
                    pass
        year_data.append((year,len(alive_cats)))
    return year_data

def main():
    sims = []
    year_data = {}
    N = 1000
    for n in range(N):
        sim = simulate()
        sims.append(simulate())
        for year in sim:
            if year[0] not in year_data.keys():
                year_data[year[0]] = []
                year_data[year[0]].append(year[1])
            else:
                year_data[year[0]].append(year[1])
        print(n)
    plt_x = []; plt_y = []
    for year in year_data:
        print("year, |cats| : %d %f"%(year, np.mean(year_data[year])))
        plt_x.append(year)
        plt_y.append(np.mean(year_data[year]))
    plt.scatter(plt_x, plt_y, c="k", alpha=0.5, marker='x',label="Cats")
    plt.xlabel("Year")
    plt.ylabel("Cats")
    plt.legend(loc='upper left')
    plt.show()



if __name__ == "__main__":
    main()
