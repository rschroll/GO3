"""
    This file is part of Gig-o-Matic

    Gig-o-Matic is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from django.urls import path

from . import views
from . import helpers

urlpatterns = [
    path('create/<int:bk>', views.CreateView.as_view(), name='gig-create'),
    path('<int:pk>/', views.DetailView.as_view(), name='gig-detail'),
    path('<int:pk>/update', views.UpdateView.as_view(), name='gig-update'),

    path('plan/<int:pk>/update/<int:val>', helpers.update_plan, name='plan-update'),
    path('plan/<int:pk>/feedback/<int:val>', helpers.update_plan_feedback, name='plan-update-feedback'),
    path('plan/<int:pk>/comment', helpers.update_plan_comment, name='plan-update-comment')
]
