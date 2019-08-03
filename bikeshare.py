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
    print('Hi there! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
            city = input('Please enter a city name to explore the data: Chicago, New York City or Washington \n').lower()
            if city in ['chicago', 'new york city', 'washington']:
                break
            else:
                print('It seems like your entry for city name is invaild.. try entering: chicago \n') 
      
    
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
            print('Please enter a month you wanted to filter by:' )
            month = input('January, february, March, April, May, June or all if you don\'t want to filter \n').lower()
            if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
                break
            else:
                 print('It seems like your entry for month is invaild.. try entering: all') 
     
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
            print('Please enter a day of the week you wanted to filter by: \n')
            day = input('Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or all if you don\'t want to filter \n').lower()
            if day in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']:
                  break
            else:
                  print('It seems like your entry for day is invaild.. try entering: sunday')
                
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
    df['day'] = df['Start Time'].dt.weekday_name 
                  
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
        df = df[df['day'] == day.title()]
                 
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('\nThe most common month for travel is...\n', common_month)
    
    # TO DO: display the most common day of week
    common_dow = df['day'].mode()[0]
    print('\nThe most common day of the week for travel is...\n', common_dow)
                  
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('\nThe most common start hour for travel is:\n', common_hour)              

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('\nThe most common start station is:\n', common_start)

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('\nThe most common end station is:\n', common_start)

    # TO DO: display most frequent combination of start station and end station trip
    common_both = df[['Start Station', 'End Station']].mode().loc[0]
    print('The most frequent combination of start station and end station trip is from {} station to {} station'.format(common_both[0], common_both[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('\nThe total travel time is: \n', total_time)   

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('\nThe mean travel time is: \n', mean_time)   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nThe counts of each user type are:\n', user_types)
    
    # As the washington data doesn't have the 'gender' and 'Birth Year', implemented an exception.
    try:
        # TO DO: Display counts of gender
        gender_count = df['Gender'].value_counts()
        print('\nThe counts of gender are:\n', gender_count)
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth_year = df['Birth Year'].min()
        print('\nThe earliest year of birth is:\n', earliest_birth_year)     

        recent_birth_year = df['Birth Year'].max()
        print('\nThe most recent year of birth is:\n', recent_birth_year)

        common_birth_year = df['Birth Year'].mode()[0]   
        print('\nThe most common year of birth is:\n', recent_birth_year)
    except:
        print('\nUnfortunately the city you choose doesn\'t have the gender and birth year information.')
   
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def show_data(df):
    """Displays orginal data 5 records at a time if the user is interested"""
    print('\nDo you want to see the original data? I can show you 5 records at a time.')
    num_count = 0
    while True:
        answer = input('Enter yes or no: ').lower()
        if answer != 'yes':
            break
        else:
            print(df.iloc[num_count:num_count + 5,:])
            num_count += 5
            print('\nDo you want to see more data?')
        
  
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
