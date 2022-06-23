
"""
Author:
Purpose:
Date：
"""


import argparse
import matplotlib.pyplot as plt
import numpy as np


def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return  argparser.parse_args()

def f1():
    years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
    gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
    plt.plot(years,gdp,color='red',marker='o',linestyle='solid')
    plt.title('GDP')
    plt.ylabel('GDP of YEAR')
    plt.show()



def barFunc():
    movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
    num_oscars = [5, 11, 3, 8, 10]
    plt.bar(range(len(movies)), num_oscars)
    plt.title("My Favorite Movies")  # add a title
    plt.ylabel("# of Academy Awards")  # label the y-axis
    plt.xticks(range(len(movies)),movies)

    plt.show()

def linePlot1():
    variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
    total_error = [x + y for x, y in zip(variance, bias_squared)]
    xs = [i for i, _ in enumerate(variance)]
    plt.plot(xs, variance, 'g-', label='variance')  # green solid line
    plt.plot(xs, bias_squared, 'r-.', label='bias^2')  # red dot-dashed line
    plt.plot(xs, total_error, 'b:', label='total error')  # blue dotted line
    plt.legend()
    plt.show()

def scatterPlot():
    friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
    minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    plt.scatter(friends, minutes)
    # label each point

    for label, friend_count, minute_count in zip(labels, friends, minutes):
        plt.annotate(label,
                     xy=(friend_count, minute_count),  # Put the label with its point
                     xytext=(5, -5),  # but slightly offset
                     textcoords='offset points')

    plt.title("Daily Minutes vs. Number of Friends")
    plt.xlabel("# of friends")
    plt.ylabel("daily minutes spent on the site")
    plt.show()


def main():
    scatterPlot()

if __name__ == '__main__':
    main()