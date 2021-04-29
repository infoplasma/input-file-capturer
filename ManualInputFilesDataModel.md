# FInstaSocialOverview

- **Description**: Fact table to represent Instagram Social Overview
- **Schema**: dbo
- **Source of Data**: csv files
- **Executing Resources**: Data Factory

| PK/FK | Attribute | DataType | Description |
| --- | --- | --- | --- |
|   | LocaleDateID |  date NULL |   |
|   | Region |  varchar(32) NULL |   |
|   | Country  |  varchar(16) NULL |   |
|   | BrandId  |  varchar(32) NULL |   |
|   | TotalImpressions  | int NULL  |  |
|   | OrganicImpressions  | int NULL   |   |
|   | PaidImpressions  | int NULL   |   |
|   | AdSpent  | float NULL   |   |
|   |TotalEngagement   | int NULL   |   |
|   | FanCount  | int NULL   |   |
|   | UniquePaidReach  | int NULL   |   |


# FAdditionalEngagement

- **Description**: A Fact table to represent Facebook Additional Engagement data
- **Schema**: dbo
- **Source of Data**: csv file
- **Executing Resources**: Data Factory

| PK/FK | Attribute | DataType | Description |
| --- | --- | --- | --- |
|   | Tracking |  nvarchar(32) NULL  |   |
|   | LocaleDateID |  date NULL  |   |
|   | BrandId |  varchar(32) NULL  |   |
|   | Region | varchar(32) NULL   |   |
|   |  WebsiteReturningVisitors | float NULL   |   |
|	| CTRforStandaloneNewsletters  | float NULL |
|	| InteractionRateFB  | float NULL |
|	| InteractionRateInstagram |  float NULL |
|	| YoutubeViewTimeMin30perc  | float NULL |
|	| MobileMAUvsInstalls |  float NULL |
|	| EngagementTargetAchievementRate |  float NULL |


# FAdditionalImpressions

- **Description**: A Fact table to represent Facebook Additional Impressions data
- **Schema**: dbo
- **Source of Data**: csv file
- **Executing Resources**: Data Factory

| PK/FK | Attribute | DataType | Description |
| --- | --- | --- | --- |
| |	LocaleDateID |  date NULL |
| |	Channel  | varchar(64)  NULL |
| |	Impressions |  int NULL |
| |	BrandId |  varchar(32)  NULL |
| |	Region |  varchar(32)  NULL |


# FFbAccountFans

- **Description**: A Fact table to represent Facebook Account Fans data
- **Schema**: dbo
- **Source of Data**: csv file
- **Executing Resources**: Data Factory

| PK/FK | Attribute | DataType | Description |
| --- | --- | --- | --- |
| | LocaleDateID | date NULL |
| | Page | varchar(64) NULL |
| | Fans | int NULL |


# FFbSocialOverview

- **Description**: A Fact table to represent Facebook Social Overview data
- **Schema**: dbo
- **Source of Data**: csv file
- **Executing Resources**: Data Factory

| PK/FK | Attribute | DataType | Description |
| --- | --- | --- | --- |
| |	LocaleDateID  | date NULL |
| |	Country |  varchar(16) NULL |
| |	TotalImpressions  | int NULL |
| |	OrganicImpressions |  int NULL |
| |	PaidImpressions |  int NULL |
| |	AdSpent |  float NULL |
| |	TotalEngagement  | int NULL |
| |	FanCount |  int NULL |
| |	UniquePaidReach |  int NULL |


# DFbManualAccount

- **Description**: A Dimension table to represent Facebook Manual Account data
- **Schema**: dbo
- **Source of Data**: csv file
- **Executing Resources**: Data Factory

| PK/FK | Attribute | DataType | Description |
| --- | --- | --- | --- |
|	|ChannelID | varchar(64)  NULL|
|	|BrandId|  varchar(32)  NULL|
|	|Country | varchar(16)  NULL|
|	|PageName | nvarchar(512)  NULL|
|	|URL|  varchar(512)  NULL|


# DYTCraftsman

- **Description**: A Dimension table to represent YoutTube Craftsman data
- **Schema**: dbo
- **Source of Data**: csv file
- **Executing Resources**: Data Factory

| PK/FK | Attribute | DataType | Description |
| --- | --- | --- | --- |
| |	LocaleDateID | date NULL|
| |	BrandId | varchar(32)  NULL|
| |	Country | varchar(16)  NULL|
| |	EstimatedCraftsmen | int NULL|


# FCRMReach

- **Description**: A Fact table to represent CRM Reach data
- **Schema**: dbo
- **Source of Data**: csv file
- **Executing Resources**: Data Factory

| PK/FK | Attribute | DataType | Description |
| --- | --- | --- | --- |
| |	LocaleDateID | date NULL |
| |	BrandId | varchar(32)  NULL |
| |	Country| varchar(32)  NULL |
| |	Emails|  int NULL |
| |	OpenRate | float NULL |
| |	ClickRate | float NULL |


# FMobileCountry

- **Description**: A Fact table to represent Mobile Country data
- **Schema**: dbo
- **Source of Data**: csv file
- **Executing Resources**: Data Factory

| PK/FK | Attribute | DataType | Description |
| --- | --- | --- | --- |
| |	LocaleDateID | date NULL|
| |	AppName | varchar(128)  NULL|
| |	BrandId | varchar(32)  NULL|
| |	Country | varchar(16)  NULL|
| |	ActiveDeviceInstalls | int NULL|


# FMobileInstalls

- **Description**: A <D/F table to represent the <what>in different formats</what>
- **Schema**: dbo
- **Source of Data**: csv file
- **Executing Resources**: Data Factory

| PK/FK | Attribute | DataType | Description |
| --- | --- | --- | --- |
| |	LocaleDateID | date NULL | 
| |	AppName | varchar(128)  NULL | 
| |	BrandId | varchar(32)  NULL | 
| |	Region|  varchar(32)  NULL | 
| |	MonthlyAndroidRating | float NULL | 
| |	MonthlyiOSRating|  float NULL | 
| |	TotalAndroidRating | float NULL | 
| |	TotaliOSRating|  float NULL | 
| |	MonthlyRatings | int NULL | 
| |	MonthlyReviews|  int NULL | 
| |	TotalRatings|  int NULL | 
| |	TotalReviews | int NULL | 


# FUserConsent

- **Description**: A Fact table to represent User Consent data
- **Schema**: dbo
- **Source of Data**: csv file
- **Executing Resources**: Data Factory

| PK/FK | Attribute | DataType | Description |
| --- | --- | --- | --- |
| | 	LocaleDateID |  date NULL |
| |	BrandId  | varchar(32)  NULL |
| |	Country  | varchar(16)  NULL |
| |	AllData  | int NULL |
| |	Consent  | int NULL |
| |	ConsentPY  | int NULL |
| |	ConsentLocal  | int NULL |
| |	TargetDelta | int NULL |


# FUserConsentChannel

- **Description**: A Fact table to represent User Consent
- **Schema**: dbo
- **Source of Data**: csv file
- **Executing Resources**: Data Factory

| PK/FK | Attribute | DataType | Description |
| --- | --- | --- | --- |
| |	LocaleDateID | date NULL |
| |	BrandId | varchar(32)  NULL |
| |	Channel|  nvarchar(512)  NULL |
| |	AllData|  int NULL |
| |	Consent | int NULL |
	
	
