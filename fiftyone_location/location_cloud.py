# *********************************************************************
# This Original Work is copyright of 51 Degrees Mobile Experts Limited.
# Copyright 2019 51 Degrees Mobile Experts Limited, 5 Charlotte Close,
# Caversham, Reading, Berkshire, United Kingdom RG4 7BY.
#
# This Original Work is licensed under the European Union Public Licence (EUPL) 
# v.1.2 and is subject to its terms as set out below.
#
# If a copy of the EUPL was not distributed with this file, You can obtain
# one at https://opensource.org/licenses/EUPL-1.2.
#
# The 'Compatible Licences' set out in the Appendix to the EUPL (as may be
# amended by the European Commission) shall be deemed incompatible for
# the purposes of the Work and the provisions of the compatibility
# clause in Article 5 of the EUPL shall not apply.
# 
# If using the Work as, or as part of, a network application, by 
# including the attribution notice(s) required under Article 5 of the EUPL
# in the end user terms of the application under an appropriate heading, 
# such notice(s) shall fulfill the requirements of that article.
# ********************************************************************

from fiftyone_pipeline_cloudrequestengine.cloudengine import CloudEngine


"""
 The deviceDetction cloud engine requires the 51Degrees
 cloudRequestEngine to be placed in a pipeline before it.
 It takes that raw JSON response and parses it to extract the
 device part. It also uses this data to generate a list of properties
"""
class LocationCloud(CloudEngine):

    def __init__(self, settings = {}):

        super(LocationCloud, self).__init__()

        self.datakey = "location"

        if "locationProvider" in settings:
            locationProvider = settings["locationProvider"]
            if locationProvider == "fiftyonedegrees":
                self.datakey = "location"
            elif locationProvider == "digitalelement":
                self.datakey = "location_digitalelement"
            else:
                raise Exception("The location provider " + locationProvider + " was not recognized.")
