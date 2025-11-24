import { Component } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';

import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';

import { LinkList } from '../link-list';

@Component({
  selector: 'app-link-list',
  templateUrl: './link-list.component.html',
  styleUrl: './link-list.component.scss',
  imports: [MatButtonModule, FontAwesomeModule]
})
export class LinkListComponent {
  constructor(public links: LinkList) { }
}
