"""
CSE 163
Daniel Lee

This file plots some basic statistics about the average price of an avocado,
as well as plot the yield of avocados and apples. All plots are against a
3 year basis, from 2015 to 2018.
"""
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()


def yield_trend(data_yield):
    """
    Plots the yield of avocados for each year between 2015 and 2018.
    """
    # Masks for avocado yield dataset
    is_2015_to_2018 = ((data_yield['Year'] >= 2015) &
                       (data_yield['Year'] <= 2018))
    is_Americas = (data_yield['Country or Area'] == 'Americas')
    is_Yield = (data_yield['Element'] == 'Yield')
    filtered_avo_yield = data_yield[is_2015_to_2018 & is_Americas & is_Yield]
    sns.relplot(x='Year', y='Value', kind='line', data=filtered_avo_yield)
    plt.ylabel("Avocado Yield (in hg/ha)")
    plt.xticks(rotation=-45)
    plt.title('Avocado Yield Trend Per Year From 2015 to 2018 (in hg/ha)')
    plt.savefig('./output/avocado_yield.png', bbox_inches='tight')


def sale_trend(data_sales):
    """
    Plots the average price of an avocado for each year between 2015 and 2018.
    """
    # Masks for avocado sales dataset
    is_US = (data_sales['region'] == 'TotalUS')
    is_2015_to_2018 = ((data_sales['year'] >= 2015) &
                       (data_sales['year'] <= 2018))
    is_conventional = ((data_sales['type'] == 'conventional') |
                       (data_sales['type'] == 'Conventional'))
    filtered_avo_sales = data_sales[is_US & is_2015_to_2018 & is_conventional]
    sns.relplot(x='year', y='AveragePrice', kind='line',
                data=filtered_avo_sales)
    plt.xlabel("Year")
    plt.ylabel("Average Avocado Price (in USD)")
    plt.xticks(rotation=-45)
    plt.title('Average Price of an Avocado from 2015 to 2018')
    plt.savefig('./output/avocado_sales.png', bbox_inches='tight')


def apple_yield_trend(apple_data_yield):
    """
    Plots the yield of apples for each year between 2015 and 2018.
    """
    # Masks for apple sales dataset (should be same as avocado sales)
    is_2015_to_2018 = ((apple_data_yield['Year'] >= 2015) &
                       (apple_data_yield['Year'] <= 2018))
    is_Americas = (apple_data_yield['Country or Area'] == 'Americas')
    is_Yield = (apple_data_yield['Element'] == 'Yield')
    filtered_apple_yield = apple_data_yield[is_2015_to_2018
                                            & is_Americas & is_Yield]
    sns.relplot(x='Year', y='Value', kind='line', data=filtered_apple_yield)
    plt.ylabel("Apple Yield (in hg/ha)")
    plt.xticks(rotation=-45)
    plt.title('Apple Yield Trend Per Year From 2015 to 2018 (in hg/ha)')
    plt.savefig('./output/apple_yield.png', bbox_inches='tight')
