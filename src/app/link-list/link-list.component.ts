import { Component, inject } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';

import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';

import { LinkList } from '../link-list';
import { Vul } from '../vul';

@Component({
  selector: 'app-link-list',
  templateUrl: './link-list.component.html',
  styleUrl: './link-list.component.scss',
  imports: [MatButtonModule, FontAwesomeModule, Vul]
})
export class LinkListComponent {
  public readonly links: LinkList = inject(LinkList);
}
