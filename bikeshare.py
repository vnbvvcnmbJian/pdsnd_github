{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello! Let's explore some US bikeshare data!\n",
      "Please choose a city you are interested in, Chicago, New york city, or Washington:New york city\n",
      "Thank you! Nice choice.\n",
      "Would you like to choose all the six months or which month would you like to explore:January\n",
      "Thank you!\n",
      "Would you like to choose all the days or which day would you like to explore:Monday\n",
      "Thank you!\n",
      "----------------------------------------\n"
     ]
    },
    {
     "ename": "AttributeError",
     "evalue": "'DatetimeProperties' object has no attribute 'weekday_name'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-2-60ae7d530021>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m    211\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    212\u001b[0m \u001b[1;32mif\u001b[0m \u001b[0m__name__\u001b[0m \u001b[1;33m==\u001b[0m \u001b[1;34m\"__main__\"\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 213\u001b[1;33m     \u001b[0mmain\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m<ipython-input-2-60ae7d530021>\u001b[0m in \u001b[0;36mmain\u001b[1;34m()\u001b[0m\n\u001b[0;32m    197\u001b[0m     \u001b[1;32mwhile\u001b[0m \u001b[1;32mTrue\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    198\u001b[0m         \u001b[0mcity\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmonth\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mday\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mget_filters\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 199\u001b[1;33m         \u001b[0mdf\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mload_data\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mcity\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmonth\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mday\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    200\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    201\u001b[0m         \u001b[0mdisplay_raw_data\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdf\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m<ipython-input-2-60ae7d530021>\u001b[0m in \u001b[0;36mload_data\u001b[1;34m(city, month, day)\u001b[0m\n\u001b[0;32m     79\u001b[0m     \u001b[0mdf\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m\"Start Time\"\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mto_datetime\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdf\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m\"Start Time\"\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     80\u001b[0m     \u001b[0mdf\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m\"month\"\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mdf\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m\"Start Time\"\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdt\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmonth\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 81\u001b[1;33m     \u001b[0mdf\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m\"day_of_week\"\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mdf\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m\"Start Time\"\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdt\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mweekday_name\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     82\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[0mmonth\u001b[0m \u001b[1;33m!=\u001b[0m\u001b[1;34m'all'\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     83\u001b[0m         \u001b[0mmonths\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m[\u001b[0m\u001b[1;34m'january'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m'february'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m'march'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m'april'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m'may'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m'june'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mAttributeError\u001b[0m: 'DatetimeProperties' object has no attribute 'weekday_name'"
     ]
    }
   ],
   "source": [
    "import time\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "CITY_DATA = { 'chicago': 'chicago.csv',\n",
    "              'new york city': 'new_york_city.csv',\n",
    "              'washington': 'washington.csv' }\n",
    "\n",
    "def get_filters():\n",
    "    \"\"\"\n",
    "    Asks user to specify a city, month, and day to analyze.\n",
    "\n",
    "    Returns:\n",
    "        (str) city - name of the city to analyze\n",
    "        (str) month - name of the month to filter by, or \"all\" to apply no month filter\n",
    "        (str) day - name of the day of week to filter by, or \"all\" to apply no day filter\n",
    "    \"\"\"\n",
    "    print('Hello! Let\\'s explore some US bikeshare data!')\n",
    "    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs\n",
    "    city=input(\"Please choose a city you are interested in, Chicago, New york city, or Washington:\")\n",
    "    city=city.lower()\n",
    "    cities=[\"chicago\",\"new york city\",\"washington\"]\n",
    "    if city in cities:\n",
    "        print(\"Thank you! Nice choice.\")\n",
    "    else:\n",
    "        city=input(\"Incorrect input. Please input the right city, Chicago, New your city, or Washington:\")\n",
    "        city=city.lower()\n",
    "    \n",
    "\n",
    "    # TO DO: get user input for month (all, january, february, ... , june)\n",
    "    month=input(\"Would you like to choose all the six months or which month would you like to explore:\")\n",
    "    month=month.lower()\n",
    "    months = ['january','february','march','april','may','june','all']\n",
    "    if month in months:\n",
    "        print(\"Thank you!\")\n",
    "    else:\n",
    "        month=input(\"Incorrect input. Please input the full name of the month (first six month in the year):\")\n",
    "        month=month.lower()\n",
    "\n",
    "    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)\n",
    "    day=input(\"Would you like to choose all the days or which day would you like to explore:\")\n",
    "    day=day.lower()\n",
    "    days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']\n",
    "    if day in days:\n",
    "        print(\"Thank you!\")\n",
    "    else:\n",
    "        day=input(\"Incorrect input. Please input the full name of the day:\")\n",
    "        day=day.lower()\n",
    "\n",
    "    print('-'*40)\n",
    "    return city, month, day\n",
    "\n",
    "def display_raw_data(df):\n",
    "    \"\"\" prompt the user whether they would like to see the raw data as specified in project instruction. If the user answers 'yes,' then the script should print 5 rows of the data at a time, then ask the user if they would like to see 5 more rows of the data. The script should continue prompting and printing the next 5 rows at a time until the user chooses 'no'. \"\"\"\n",
    "    i = 0\n",
    "    raw = input(\"Would you like to check the raw data? Yes or No:\\n\") # TO DO: convert the user input to lower case using lower() function\n",
    "    raw=raw.lower()\n",
    "    pd.set_option('display.max_columns',200)\n",
    "\n",
    "    while True:            \n",
    "        if raw == 'no':\n",
    "            break\n",
    "        print(df[i:i+5]) # TO DO: appropriately subset/slice your dataframe to display next five rows\n",
    "        raw = input('Would you like to find see more data? Yes or No:\\n').lower() # TO DO: convert the user input to lower case using lower() function\n",
    "        i += 5\n",
    "\n",
    "def load_data(city, month, day):\n",
    "    \"\"\"\n",
    "    Loads data for the specified city and filters by month and day if applicable.\n",
    "\n",
    "    Args:\n",
    "        (str) city - name of the city to analyze\n",
    "        (str) month - name of the month to filter by, or \"all\" to apply no month filter\n",
    "        (str) day - name of the day of week to filter by, or \"all\" to apply no day filter\n",
    "    Returns:\n",
    "        df - Pandas DataFrame containing city data filtered by month and day\n",
    "    \"\"\"\n",
    "    df = pd.read_csv(CITY_DATA[city])\n",
    "    df[\"Start Time\"] = pd.to_datetime(df[\"Start Time\"])\n",
    "    df[\"month\"] = df[\"Start Time\"].dt.month\n",
    "    df[\"day_of_week\"] = df[\"Start Time\"].dt.weekday_name\n",
    "    if month !='all':\n",
    "        months = ['january','february','march','april','may','june']\n",
    "        month = months.index(month)+1\n",
    "        df = df[df[\"month\"]==month]\n",
    "          \n",
    "    if day !='all':\n",
    "        df = df[df[\"day_of_week\"]==day.title()]\n",
    "\n",
    "    return df\n",
    "\n",
    "\n",
    "def time_stats(df):\n",
    "    \"\"\"Displays statistics on the most frequent times of travel.\"\"\"\n",
    "\n",
    "    print('\\nCalculating The Most Frequent Times of Travel...\\n')\n",
    "    start_time = time.time()\n",
    "\n",
    "    # TO DO: display the most common month\n",
    "    #df[\"month\"]=pd.to_datetime(df[\"Start Time\"]).dt.month\n",
    "    months = ['january','february','march','april','may','june']\n",
    "    popular_month = df[\"month\"].mode()[0]\n",
    "    print(\"The most common month:\",months[popular_month-1].capitalize())\n",
    "   \n",
    "\n",
    "    # TO DO: display the most common day of week\n",
    "    #df[\"day_of_week\"] = pd.to_datetime(df[\"Start Time\"]).dt.weekday_name\n",
    "    popular_day_of_week = df[\"day_of_week\"].mode()[0]\n",
    "    print(\"The most common day of week:\",popular_day_of_week)\n",
    "\n",
    "    # TO DO: display the most common start hour\n",
    "    df[\"hour\"]=pd.to_datetime(df[\"Start Time\"]).dt.hour\n",
    "    popular_hour=df[\"hour\"].mode()[0]\n",
    "    print(\"The most common start hour:\",popular_hour)\n",
    "\n",
    "    print(\"\\nThis took %s seconds.\" % (time.time() - start_time))\n",
    "    print('-'*40)\n",
    "\n",
    "\n",
    "def station_stats(df):\n",
    "    \"\"\"Displays statistics on the most popular stations and trip.\"\"\"\n",
    "\n",
    "    print('\\nCalculating The Most Popular Stations and Trip...\\n')\n",
    "    start_time = time.time()\n",
    "\n",
    "    # TO DO: display most commonly used start station\n",
    "    popular_start_station=df[\"Start Station\"].mode()[0]\n",
    "    print(\"The most commonly used start station:\",popular_start_station)\n",
    "\n",
    "    # TO DO: display most commonly used end station\n",
    "    popular_end_station=df[\"End Station\"].mode()[0]\n",
    "    print(\"The most commonly used end station:\",popular_end_station)\n",
    "\n",
    "    # TO DO: display most frequent combination of start station and end station trip\n",
    "    df[\"Trip\"]=df[\"Start Station\"]+\" to \"+df[\"End Station\"]\n",
    "    popular_trip=df[\"Trip\"].mode()[0]\n",
    "    print(\"The most frequent combination of start station and end station trip is:\",popular_trip)\n",
    "\n",
    "    print(\"\\nThis took %s seconds.\" % (time.time() - start_time))\n",
    "    print('-'*40)\n",
    "\n",
    "\n",
    "def trip_duration_stats(df):\n",
    "    \"\"\"Displays statistics on the total and average trip duration.\"\"\"\n",
    "\n",
    "    print('\\nCalculating Trip Duration...\\n')\n",
    "    start_time = time.time()\n",
    "\n",
    "    # TO DO: display total travel time\n",
    "    total_travel_time = df[\"Trip Duration\"].sum()\n",
    "    print(\"The total travel time:\",total_travel_time)\n",
    "\n",
    "    # TO DO: display mean travel time\n",
    "    mean_travel_time = df[\"Trip Duration\"].mean()\n",
    "    print(\"The mean travel time:\",mean_travel_time)\n",
    "\n",
    "    print(\"\\nThis took %s seconds.\" % (time.time() - start_time))\n",
    "    print('-'*40)\n",
    "\n",
    "\n",
    "def user_stats(df):\n",
    "    \"\"\"Displays statistics on bikeshare users.\"\"\"\n",
    "\n",
    "    print('\\nCalculating User Stats...\\n')\n",
    "    start_time = time.time()\n",
    "\n",
    "    # TO DO: Display counts of user types\n",
    "    user_types = df[\"User Type\"].value_counts()\n",
    "    print(\"User Type:\\n\",user_types)\n",
    "\n",
    "    # TO DO: Display counts of gender\n",
    "    columns=df.columns\n",
    "    if \"Gender\" not in columns:\n",
    "        df[\"Gender\"]=\"no idea\"\n",
    "        print(\"Sorry, I have no idea about the user gender.\")\n",
    "    else:\n",
    "        Gender = df[\"Gender\"].value_counts()\n",
    "        print(\"Gender:\\n\",Gender)\n",
    "\n",
    "    # TO DO: Display earliest, most recent, and most common year of birth\n",
    "    if \"Birth Year\" in columns:\n",
    "        earliest_year_of_birth=df[\"Birth Year\"].min()\n",
    "        recent_year_of_birth=df[\"Birth Year\"].max()\n",
    "        common_year_of_birth=df[\"Birth Year\"].mode()[0]\n",
    "        print(\"The earliest year of birth:\\n\",earliest_year_of_birth.astype(\"int\"))\n",
    "        print(\"The most recent year of birth:\\n\",recent_year_of_birth.astype(\"int\"))\n",
    "        print(\"The most common year of birth:\\n\",common_year_of_birth.astype(\"int\"))\n",
    "    else:\n",
    "        df[\"Birth Year\"]=0\n",
    "        print(\"Sorry, I have no idea about the users' birth year.\")\n",
    "\n",
    "    print(\"\\nThis took %s seconds.\" % (time.time() - start_time))\n",
    "    print('-'*40)\n",
    "\n",
    "\n",
    "def main():\n",
    "    while True:\n",
    "        city, month, day = get_filters()\n",
    "        df = load_data(city, month, day)\n",
    "\n",
    "        display_raw_data(df)\n",
    "        time_stats(df)\n",
    "        station_stats(df)\n",
    "        trip_duration_stats(df)\n",
    "        user_stats(df)\n",
    "\n",
    "        restart = input('\\nWould you like to restart? Enter yes or no.\\n')\n",
    "        if restart.lower() != 'yes':\n",
    "            break\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
