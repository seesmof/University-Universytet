listing
- id: key
- user: user.id
- type: house | flat | condo
- rooms: 1 | 2 | 3
- area: 12 | 17 | 23
- decade: 00 | 10 | 20
- style: Biblical | Missionary | Monastic
- photo: str

leeting
- id: key
- client: user.id
- seller: user.id
- listing: listing.id
- status: pending | approved | canceled
- score: good | great | well

user
- id: key
- name: str
- password: str
- type: user | manager