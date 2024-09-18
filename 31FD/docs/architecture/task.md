Програмне забезпечення продажу та придбання нерухомості. Всю нерухомість поділено на приватні будинки, окремі квартири та квартири в новобудовах. Приватні будинки та окремі квартири можуть виставлятися на продаж звичайними користувачами. Квартири в новобудовах можуть виставлятися тільки спеціальними менеджерами. Користувачі можуть подавати заявки на перегляд житла, передивлятися стан заявок, а також після перегляду виставляти оцінку. Власники можуть передивлятися заявки на всі їхні пропозиції або на обрані, підтверджувати перегляд або скасовувати, знімати пропозиції (кількість кімнат, площа, рік будівництва, зображення, планування, тощо), змінювати.

# requirements

- listing can be house | flat | condo
- condo can be listed only by manager
- user can request meeting 
- meeting must have status pending | approved | canceled
- meeting must have score good | great | well
- meeting score must be available only if status != pending
- owners see meeting requests for all listings or only selected
- owners can change meeting status 
- owners can edit listings 
- owners can delete listings
- listing must include rooms number, area, deacde, image, style

# minimum

- market 
  - listings view
- meeting 
  - view only selected listing
  - ability to sort by name, change status
  - if meeting.status == approved: ability to set score by user
- profile 
  - view and edit personal info of user
  - view and edit listings: either selected or own
    - add new listing, allow listing.type == new only for user.type == manager
    - delete listings 
    - modify listings 
  - request manager status button if have >= 3 listings

# extra, if JESUS willing

- see deleted listings 
- market add search bar and filters 
- listing add image spinner 
- meeting add date picker 
- listing see seller and go to their profile
- user make list of selected listings, display them
- info section about why listings are free and what it all means
- ability to change UI language: Ukrainian | English
- in login screen remember users and quickly login
- try making a copy of DB in XML files