from django.test import TestCase
from sciwms.apps.wms.tests import *


class TestUgrid(TestCase):

    def setUp(self):
        add_server()
        add_group()
        add_user()
        self.dataset = add_dataset("201220109.nc")

    def tearDown(self):
        self.dataset.clear_cache()

    def test_web_remove(self):
        response = self.client.get('/wms/remove_dataset/?id=test&username=testuser&password=test')
        self.assertEqual(response.status_code, 200)

    def test_facets(self):
        response = self.client.get('/wms/datasets/test/?LAYERS=u%2Cv&TRANSPARENT=TRUE&STYLES=facets_average_jet_None_None_cell_False&TIME=&ELEVATION=0&SERVICE=WMS&VERSION=1.1.1&REQUEST=GetMap&FORMAT=image%2Fpng&SRS=EPSG%3A3857&BBOX=-8543030.3273202,5492519.0747705,-8401010.3287862,5542356.0172055&WIDTH=929&HEIGHT=326')
        self.assertEqual(response.status_code, 200)

    def test_pcolor(self):
        response = self.client.get('/wms/datasets/test/?LAYERS=u%2Cv&TRANSPARENT=TRUE&STYLES=pcolor_average_jet_None_None_cell_False&TIME=&ELEVATION=0&SERVICE=WMS&VERSION=1.1.1&REQUEST=GetMap&FORMAT=image%2Fpng&SRS=EPSG%3A3857&BBOX=-8543030.3273202,5492519.0747705,-8401010.3287862,5542356.0172055&WIDTH=929&HEIGHT=326')
        self.assertEqual(response.status_code, 200)

    def test_contours(self):
        response = self.client.get('/wms/datasets/test/?LAYERS=u%2Cv&TRANSPARENT=TRUE&STYLES=contours_average_jet_None_None_cell_False&TIME=&ELEVATION=0&SERVICE=WMS&VERSION=1.1.1&REQUEST=GetMap&FORMAT=image%2Fpng&SRS=EPSG%3A3857&BBOX=-8543030.3273202,5492519.0747705,-8401010.3287862,5542356.0172055&WIDTH=929&HEIGHT=326')
        self.assertEqual(response.status_code, 200)

    def test_filledcontours(self):
        response = self.client.get('/wms/datasets/test/?LAYERS=u%2Cv&TRANSPARENT=TRUE&STYLES=filledcontours_average_jet_None_None_cell_False&TIME=&ELEVATION=0&SERVICE=WMS&VERSION=1.1.1&REQUEST=GetMap&FORMAT=image%2Fpng&SRS=EPSG%3A3857&BBOX=-8543030.3273202,5492519.0747705,-8401010.3287862,5542356.0172055&WIDTH=929&HEIGHT=326')
        self.assertEqual(response.status_code, 200)

    def test_vectors(self):
        response = self.client.get('/wms/datasets/test/?LAYERS=u%2Cv&TRANSPARENT=TRUE&STYLES=vectors_average_jet_None_None_cell_False&TIME=&ELEVATION=0&SERVICE=WMS&VERSION=1.1.1&REQUEST=GetMap&FORMAT=image%2Fpng&SRS=EPSG%3A3857&BBOX=-8543030.3273202,5492519.0747705,-8401010.3287862,5542356.0172055&WIDTH=929&HEIGHT=326')
        self.assertEqual(response.status_code, 200)

    def test_getLegend(self):
        pass

    def test_getCaps(self):
        response = self.client.get('/wms/datasets/test/?REQUEST=GetCapabilities')
        self.assertEqual(response.status_code, 200)
