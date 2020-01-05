import time
import pandas as pd

import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    i = 1
    while i < 888:
        city = input("Choose a city: 'chicago', 'new york city' or 'washington':    ").lower()
        valid_cities = ("chicago","new york city","washington")
        if city in valid_cities:
            print("** Valid Input City Verified **")
            break
        else:
            print("please try again")

    # TO DO: get user input for month (all, january, february, ... , june)
    i = 1
    while i < 888:
        month = input("Choose a month:  'january', 'february', 'march', 'april', 'may', 'june', or 'all':    ").lower()
        valid_months = ("january", "february", "march", "april", "may", "june", "all")
        if month in valid_months:
            print("** Valid Input Month Verified **")
            break
        else:
            print("please try again")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    i = 1
    while i < 888:
        day = input("Choose a day:  'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', or 'all':    ").lower()
        valid_days = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all")
        if day in valid_days:
            print("** Valid Input Day Verified **")
            break
        else:
            print("please try again")



    print(city, month, day)
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month:', popular_month)


    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Day of Week:', popular_day)


    # TO DO: display the most common start hour

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    #popular_s_station = df['Start Station'].mode()[0]
    #popular_s_station = df['Start Station'].value_counts().nlargest(n=1).values[0]
    popular_s_station = df['Start Station'].value_counts().idxmax()
    print('Most Popular Start Station:', popular_s_station)


    # TO DO: display most commonly used end station
    #popular_e_station = df['End Station'].mode()[0]
    popular_e_station = df['End Station'].value_counts().idxmax()
    print('Most Popular End Station:', popular_e_station)

    # TO DO: display most frequent combination of start station and end station trip
    # common_routes = df[['Start Station', 'End Station']].mode().loc[0]
    common_routes = (df['Start Station'] + " -to- " + df['End Station']).mode()[0]
    print('The most common route in this data set is: ', common_routes)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel)

    # TO DO: display mean travel time
    avg_travel = df['Trip Duration'].mean()
    print('Average Travel Time:', avg_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    # print value counts for each user type
    user_types = df['User Type'].value_counts()
    print(user_types)

    if "Gender" in df.columns:
        # TO DO: Display counts of gender
        gender_counts = df['Gender'].value_counts()
        print(gender_counts)
    else:
        print('Gender does not exist in this dataset!')
        # TO DO: Display earliest, most recent, and most common year of birth

    if "Birth Year" in df.columns:
        common_year = df['Birth Year'].mode()[0]
        print('Most Common Year of Rider:', common_year)

        old_year = df['Birth Year'].min()
        print('Earliest Year of Rider (Oldest Rider):', old_year)

        young_year = df['Birth Year'].max()
        print('Latest Year of Rider (Youngest Rider):', young_year)
    else:
        print('Birth Year does not exist in this dataset!')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_raw_data(df):

    user_feedback = input("Would you like to see 5 rows of data?\nPlease select 'yes' or 'no':  ").lower()

    while True:
        if user_feedback not in ('yes', 'no'):
            print("please try again")
            user_feedback = input("Would you like to see 5 rows of data?\nPlease select 'yes' or 'no':  ").lower()
        else:
            print("** Valid Response Accepted Accepted **\n")
            break


    if user_feedback == 'yes':
        start_range = 0
        end_range = 5
        print(df.iloc[start_range:end_range])
        start_range += 5
        end_range += 5

        while True:
            more_feedback = input("Would you like to see 5 MORE rows of data?\nPlease select 'yes' or 'no':  ").lower()

            if more_feedback not in ('yes', 'no'):
                print("please try again")
                more_feedback = input("Would you like to see 5 MORE rows of data?\nPlease select 'yes' or 'no':  ").lower()
            else:
                print("** Valid Response Accepted Accepted **\n")

            if more_feedback == 'yes':
                print(df.iloc[start_range:end_range])
                start_range += 5
                end_range += 5
            else:
                break
    else:
        print("Ok, maybe next time.\n")



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
