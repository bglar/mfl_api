Facility Reports
===================
Facility count by county, facility count by constituency, facility count by owner types are among the reports that can be generate from MFL v2.

There are number of reports that can be gotten from MFL v2:


Facility Count by County
--------------------------
``URL`` ``GET`` ``api/reporting/?report_type=facility_count_by_county``

Sample Expected Data

.. code-block:: javascript

    {
       {
            "total": 8361,
            "results": [
                {
                    "number_of_facilities": 784,
                    "county_name": "NAIROBI"
                },
                {
                    "number_of_facilities": 114,
                    "county_name": "NYAMIRA"
                }
            ]
        }
    }

Facility Count by Constituency
--------------------------------
``URL`` ``GET`` ``api/reporting/?report_type=facility_count_by_consituency``

Sample Expected Data

.. code-block:: javascript


    {
        "total": 8361,
        "results": [
            {
                "number_of_facilities": 9,
                "constituency_name": "MATHARE"
            },
            {
                "number_of_facilities": 123,
                "constituency_name": "STAREHE"
            },
            {
                "number_of_facilities": 58,
                "constituency_name": "KAMUKUNJI"
            }
        ]
    }

You can also filter by county by appending the county to the URL as shown below
``URL`` ``GET`` ``api/reporting/?report_type=facility_count_by_consituency&filters=county=<county_id>``

Sample Expected Data (Nyamira county)

.. code-block:: javascript

        {
            "total": 114,
            "results": [
                {
                    "number_of_facilities": 32,
                    "constituency_name": "BORABU"
                },
                {
                    "number_of_facilities": 26,
                    "constituency_name": "NORTH MUGIRANGO"
                },
                {
                    "number_of_facilities": 21,
                    "constituency_name": "WEST MUGIRANGO"
                },
                {
                    "number_of_facilities": 35,
                    "constituency_name": "KITUTU MASABA"
                }
            ]
        }



Facility Count by Owner Category
---------------------------------
To get a report of the facilities count bu owner category
``GET`` the ``URL``

Sample Expected Data

.. code-block:: javascript

        {
            "total": 8361,
            "results": [
                {
                    "number_of_facilities": 0,
                    "owner_category": "Other"
                },
                {
                    "number_of_facilities": 268,
                    "owner_category": "Non-Governmental Organizations"
                },
                {
                    "number_of_facilities": 3226,
                    "owner_category": "Private Institutions and Private Practice"
                },
                {
                    "number_of_facilities": 853,
                    "owner_category": "Faith Based Organization"
                },
                {
                    "number_of_facilities": 356,
                    "owner_category": "Other Public Institution"
                },
                {
                    "number_of_facilities": 3658,
                    "owner_category": "Ministry of Health"
                }
            ]
        }


Facility count by facility type
----------------------------------

It is also possible to get the count of facilities by their owner types:
``GET`` the ``URL`` ``api/reporting/?report_type=facility_count_by_facility_type``

Sample Expected Data

.. code-block:: javascript

    {
        "total": 8361,
        "results": [
            {
                "number_of_facilities": 119,
                "type_category": "District Hospital"
            },
            {
                "number_of_facilities": 901,
                "type_category": "Health Centre"
            },
            {
                "number_of_facilities": 3808,
                "type_category": "Dispensary"
            },
            {
                "number_of_facilities": 2735,
                "type_category": "Medical Clinic"
            },
            {
                "number_of_facilities": 196,
                "type_category": "Other Hospital"
            },
            {
                "number_of_facilities": 119,
                "type_category": "Sub-District Hospital"
            }
        ]
    }



Facility count by owners
----------------------------------
One can be able to get the number of facilities by owners

To get this report ``GET`` the ``URL`` ``api/reporting/?report_type=facility_count_by_owner``

Sample Expceted Response

.. code-block:: javascript

    {
        "total": 8361,
        "results": [
            {
                "owner": "State Coorporation",
                "number_of_facilities": 5
            },
            {
                "owner": "Private Enterprise (Institution)",
                "number_of_facilities": 1203
            },
            {
                "owner": "NOT IN LIST",
                "number_of_facilities": 0
            },
            {
                "owner": "Humanitarian Agencies",
                "number_of_facilities": 3
            },
            {
                "owner": "Private Practice - Unspecified",
                "number_of_facilities": 179
            }
        ]
    }



Facility types by counties detailed reports
--------------------------------------------------
To get this report do a ``GET`` to the ``URL`` ``/api/reporting/?report_type=facility_count_by_facility_type_detailed``

Sample Expected data

..  code-block:: javascript

    {
        "total": [],
        "results": [
            {
                "county": "NAIROBI",
                "facilities": [
                    {
                        "number_of_facilities": 3,
                        "facility_type": "District Hospital"
                    }
                ]
            },
            {
                "county": "Kiambu",
                "facilities": [
                    {
                        "number_of_facilities": 3,
                        "facility_type": "District Hospital"
                    }
                ]
            },
            {
                "county": "Wajir",
                "facilities": [
                    {
                        "number_of_facilities": 3,
                        "facility_type": "District Hospital"
                    }
                ]
            }
        ]
    }


Facility keph levels reports
-------------------------------
``GET`` the ``URL`` ``api/reporting/?report_type=facility_keph_level_report``


Sample Expected Response data

.. code-block:: javascript

    {
        "total": [],
        "results": [
            {
                "county": "NAIROBI",
                "facilities": [
                    {
                        "keph_level": "Not Classified",
                        "number_of_facilities": 0
                    },
                    {
                        "keph_level": "Level 6",
                        "number_of_facilities": 0
                    },
                    {
                        "keph_level": "Level 5",
                        "number_of_facilities": 0
                    },
                    {
                        "keph_level": "Level 4",
                        "number_of_facilities": 0
                    },
                    {
                        "keph_level": "Level 3",
                        "number_of_facilities": 0
                    },
                    {
                        "keph_level": "Level 2",
                        "number_of_facilities": 0
                    }
                ]
            },
            {
                "county": "KIAMBU",
                "facilities": [
                    {
                        "keph_level": "Not Classified",
                        "number_of_facilities": 0
                    },
                    {
                        "keph_level": "Level 6",
                        "number_of_facilities": 0
                    },
                    {
                        "keph_level": "Level 5",
                        "number_of_facilities": 0
                    },
                    {
                        "keph_level": "Level 4",
                        "number_of_facilities": 0
                    },
                    {
                        "keph_level": "Level 3",
                        "number_of_facilities": 0
                    },
                    {
                        "keph_level": "Level 2",
                        "number_of_facilities": 0
                    }
                ]
            }
        ]
    }


Facility report by county constituencies
----------------------------------------
``GET`` the ``URL`` ``api/reporting/?report_type=facility_constituency_report``

Sample Expected data

..  code-block:: javascript

    {
        "total": [],
        "results": [
            {
                "county": "NAIROBI",
                "facilities": [
                    {
                        "constituency": "MATHARE",
                        "number_of_facilities": 9
                    },
                    {
                        "constituency": "STAREHE",
                        "number_of_facilities": 123
                    },
                    {
                        "constituency": "KAMUKUNJI",
                        "number_of_facilities": 58
                    }
                ]
            },
            {
                "county": "HOMA BAY",
                "facilities": [
                    {
                        "constituency": "SUBA",
                        "number_of_facilities": 27
                    },
                    {
                        "constituency": "MBITA",
                        "number_of_facilities": 35
                    },
                    {
                        "constituency": "NDHIWA",
                        "number_of_facilities": 29
                    }
                ]

            }
        ]
    }

Report of Facility Upgrades and Downgrades
-------------------------------------------

URL
``api/reporting/upgrades_downgrades``


Sample Expexcted Data

..  code-block:: javascript

    {

        "total_number_of_changes": 100,
        "results": [
            {
            "county": "Nairobi",
            "changes": 10
            },
            {
                "county": "Kiambu",
                "changes": 7
            },
            {
                "county": "Embu",
                "changes": 67
            }
        ]
    }


Expected Response code:
    HTTP 200 OK


Filtering
+++++++++++++++++++++++++++++++++++++++++++++++++
The url supports filtering for upgrades and downgrades.

To get upgrades:
Do a  a get to the url
``api/reporting/upgrades_downgrades/?upgrade=True``

To get the downgrades

Do a ``GET`` to the URL
``api/reporting/upgrades_downgrades/?downgrade=True``


Filtering by counties
+++++++++++++++++++++++
``api/reporting/upgrades_downgrades/?county=<county_id>``

Sample Expected Data

..  code-block:: javascript

    {
        "total_facilities_changed": 3,
        "facilities": [
            {
                "name": "Endbeess district Hospital",
                "code": 14455,
                "current_keph_level": 4,
                "previous_keph_level": 5,
                "current_facility_type": "Distrcict Hospital",
                "previous_facility_type": "Health Centre",
                "reason": "Increase in bed capacity"

            },
            {
                "name": "Kwanaza district Hospital",
                "code": 14456,
                "current_keph_level": 3,
                "previous_keph_level": 4,
                "current_facility_type": "Distrcict Hospital",
                "previous_facility_type": "Health Centre",
                "reason": "Increase in bed capacity"

            },
            {
                "name": "Kulamawe Nursing Home",
                "code": 14457,
                "current_keph_level": 4,
                "previous_keph_level": 5,
                "current_facility_type": "Distrcict Hospital",
                "previous_facility_type": "Health Centre",
                "reason": "Increase in bed capacity"

            }
        ]
    }

The report on counties is  also filterable for upgrades and donwgrades
Like so ``api/reporting/upgrades_downgrades/?county=<county_id>&upgrade=True`` for upgrades.

Or ``api/reporting/upgrades_downgrades/?county=<county_id>&downgrade=True`` for downgrades.

