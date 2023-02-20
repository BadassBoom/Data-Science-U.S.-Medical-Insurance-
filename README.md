# Insurance-Analyzer

This Python program reads a csv file containing health insurance information and performs various analyses of the data.

## Dependencies

* Python 3.x
* **'csv'** module (included with Python)

## Usage

1. Clone this repository or download the **'insurance.csv'** file and **'insurance_analyzer.py'** file into the same directory.
1. Run the **'insurance_analyzer.py'** file with Python 3.x.
1. The program will output the following analyses of the data:
  * The average age of the patients
  * The number of male and female patients
  * The difference in average cost between smokers and non-smokers
  * The unique regions of the patients
  * The average age of patients with at least one child
  * The average yearly medical insurance charges of the patients
  
## Example

```
    $ python insurance_analyzer.py
    Average Patient Age: 39.21 years
    Number of males in the list: 676
    Number of females in the list: 662
    Average Insurance Cost For Smokers: $32050.23 dollars.
    Average Insurance Cost For Non-smokers: $8434.27 dollars.
    Unique Regions: ['southwest', 'southeast', 'northwest', 'northeast']
    Average patients age who have at least one child: 39
    Average Yearly Medical Insurance Charges: 13270.42 dollars.
```
